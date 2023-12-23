import io
import re
import copy

import chess
import chess.pgn
import urllib
import asyncio


from js import document
from pyodide.http import pyfetch


MISTAKE_REGEX = re.compile("(Inaccuracy|Mistake|Blunder)\. [KQRBN]?[a-h][1-8] was best.")


async def get_study_pgn(study_id):
    endpoint = f"https://lichess.org/api/study/{study_id}.pgn"
    resp = await pyfetch(url=endpoint, method="GET")
    study_text = await resp.text()
    return study_text 


def add_variation(game, variation):
    node = game.add_variation(chess.Move.from_uci(copy.deepcopy(variation.move.uci())))
    for idx, move in enumerate(variation.mainline()):
        if idx > 5:
            continue
        node = node.add_variation(chess.Move.from_uci(copy.deepcopy(move.uci())))
        

def export_mistakes(analysed_game, exporter):
    previous_move = None
    for move in analysed_game.mainline():
        if not previous_move:
            previous_move = move
            continue

        is_nag_blunder = bool(len(move.nags.intersection(set([2,4]))))
        if MISTAKE_REGEX.search(move.comment) or is_nag_blunder:
            export_game = chess.pgn.Game()
            export_game.headers = copy.deepcopy(analysed_game.headers)
            export_game.headers["FEN"] = copy.deepcopy(previous_move.board().fen())
            for variation in previous_move.variations[::-1]:
                add_variation(export_game, variation)
            export_game.accept(exporter)
        previous_move = move


async def download_mistake_pgn(*args, **kws):
  study_field = document.querySelector("#study-id-input")
  study_id = study_field.value
  exporter = chess.pgn.StringExporter()
  study_text = await get_study_pgn(study_id)
  input_pgn = io.StringIO(study_text)

  has_games = True
  while has_games:
      current_game = chess.pgn.read_game(input_pgn)
      if current_game is None:
          has_games = False
      else:
          export_mistakes(current_game, exporter)
  # download_link = document.querySelector("#download-link")
  download_link = document.createElement("a")
  download_link.href = "data:application/octet-stream,"+urllib.parse.quote(str(exporter), safe='~()*!\'')
  download_link.download = 'my_mistakes.pgn'
  download_link.click()

async def on_click(evt):
  await download_mistake_pgn()