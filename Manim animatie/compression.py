import string
from manim import *

class Compression(Scene):
    def construct(self):

        #objecten voor animatie
        textOIII = Text("OIII", font_size=24).shift(LEFT * 2)
        textSII = Text("SII", font_size=24).shift(LEFT * 2, UP * 2)
        textHa = Text("Ha", font_size=24).shift(LEFT * 2, DOWN * 2)

        BallOIII = Circle(radius=0.7, color=BLUE, fill_opacity=0.5).shift(LEFT * 2)
        BallSII = Circle(radius=0.7, color=RED, fill_opacity=0.5).shift(LEFT * 2, UP * 2)
        BallHa = Circle(radius=0.7, color=GREEN, fill_opacity=0.5).shift(LEFT * 2, DOWN * 2)
        BallPulsar = Circle(radius=8, color=WHITE, fill_opacity=0.7).shift(LEFT * 12)

        OIII = VGroup(BallOIII, textOIII)
        SII = VGroup(BallSII, textSII)
        Ha = VGroup(BallHa, textHa)

        ball1 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 2)
        ball2 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 2.3, UP * 0.5)
        ball3 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 1.8, DOWN * 0.5)
        ball4 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 3.2, UP * 0.6)
        ball5 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 2.9, DOWN * 0.6)
        ball6 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 3.5, UP * 1.8)
        ball7 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 3.8, DOWN * 1.8)
        ball8 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 4.1, UP * 1.3)
        ball9 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 4.4, DOWN * 1.6)
        ball10 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 4.7, UP * 1.9)
        ball11 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 5, DOWN * 1.9)
        ball12 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 2.3, UP * 1.6)
        ball13 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 2.6, DOWN * 1.3)
        ball14 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 5.9, UP * 1.8)
        ball15 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 6.2, DOWN * 1.8)
        ball16 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 3.9, DOWN * 0.1)
        ball17 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 4.3, UP * 0.6)
        ball18 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 4.8, DOWN * 0.5)
        ball19 = Circle(radius=0.2, color=GREY_BROWN, fill_opacity=0.5).shift(RIGHT * 5.2, UP * 0.6)

        #tekenen objecten
        self.play(Create(ball1), Create(ball2), Create(ball3), Create(ball4), Create(ball5), Create(ball6), 
                  Create(ball7), Create(ball8), Create(ball9), Create(ball10), Create(ball11), Create(ball12), 
                  Create(ball13), Create(ball14), Create(ball15), Create(ball16), Create(ball17), Create(ball18), Create(ball19),
                  Create(OIII), Create(SII), Create(Ha), Create(BallPulsar))
        self.wait(2)

        #animeren objecten
        self.play(OIII.animate.shift(RIGHT *4).set_fill(opacity=0.9), 
                  Ha.animate.shift(RIGHT *1), 
                  SII.animate.shift(RIGHT *1),
                ball1.animate.shift(RIGHT * 1.35).set_fill(opacity=0.9), 
                ball2.animate.shift(RIGHT * 0.7).set_fill(opacity=0.9), 
                ball3.animate.shift(RIGHT * 1.2).set_fill(opacity=0.9),
                ball4.animate.shift(RIGHT * 0.4).set_fill(opacity=0.9), 
                ball5.animate.shift(RIGHT * 0.65).set_fill(opacity=0.9),
                ball16.animate.shift(RIGHT * 0.1).set_fill(opacity=0.85),
                rate_func=smooth, run_time=3)
        
        self.wait(3)