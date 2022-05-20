from pysudoku import Puzzle

def test_find_next_empty():
    a = Puzzle()
    assert a.find_next_empty() == (0,0)

    b = Puzzle([
        [1,2,3,4,5,6,7,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ])
    assert b.find_next_empty() == (0,7)

    c = Puzzle([
        [i for i in range(1,10)] for i in range(9)
    ])
    assert c.find_next_empty() == (81,81)

if __name__ == "__main__":
    test_find_next_empty()