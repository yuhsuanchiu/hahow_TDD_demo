import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from models import Board
from datetime import datetime

URL ='https://www.ptt.cc/bbs/index.html'


def get_ptt_boards():
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text)
    result = []
    for ele in soup.find_all(name='div', attrs={'class': 'board-name'}):
        result.append(ele.text)
    return result


def insert_ptt_board(name: str, session: Session):
    board = Board(
        name=name,
        created_time=datetime.now()
    )
    session.add(board)
