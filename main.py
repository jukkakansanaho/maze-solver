from canvas import Window, Point, Line

def main():
    screen_x = 800
    screen_y = 600
    window = Window(screen_x, screen_y)
    window.draw_line(Line(Point(100, 100), Point(200, 200)))
    window.wait_for_close()

if __name__ == "__main__":
    main()
