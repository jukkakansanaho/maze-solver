import unittest
from canvas import Window, Point, Line

class TestMazeSolver(unittest.TestCase):
    def test_draw_line(self):
        w = Window(800, 600)
        l1 = w.draw_line(Line(Point(100, 100), Point(200, 200)))
        #w1.wait_for_close() 
        #expected = Window(800, 600)
        l2 = w.draw_line(Line(Point(100, 100), Point(200, 200)))
        self.assertEqual(l1, l2)
        w.wait_for_close()
    
    def test_draw_lines(self):
        w = Window(800, 600)
        l1 = w.draw_line(Line(Point(100, 100), Point(200, 200)))
        l2 = w.draw_line(Line(Point(200, 200), Point(400, 100)), "red")

        l3 = w.draw_line(Line(Point(100, 100), Point(200, 200)))
        l4 = w.draw_line(Line(Point(200, 200), Point(400, 100)), "red")
        self.assertEqual(l1, l3)
        self.assertEqual(l2, l4)
        w.wait_for_close()

if __name__ == '__main__':
    unittest.main()
