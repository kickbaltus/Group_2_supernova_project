from manim import *

class SupernovaCollapse(Scene):
    def construct(self):
        star = Circle(radius=2, color=WHITE)
        self.play(Create(star))
        self.wait(0.5)

        gravity_arrows = VGroup()
        for angle in range(0, 360, 45):
            arrow = Arrow(
                start=2.8 * RIGHT,
                end=1.2 * RIGHT,
                buff=0
            )
            arrow.rotate(angle * DEGREES)
            arrow.set_color(BLUE)
            gravity_arrows.add(arrow)

        self.play(LaggedStart(*[Create(a) for a in gravity_arrows]))
        self.wait(0.5)

        pressure_arrows = VGroup()
        for angle in range(0, 360, 45):
            arrow = Arrow(
                start=1.2 * RIGHT,
                end=2.8 * RIGHT,
                buff=0
            )
            arrow.rotate(angle * DEGREES)
            arrow.set_color(RED)
            pressure_arrows.add(arrow)

        self.play(LaggedStart(*[Create(a) for a in pressure_arrows]))
        self.wait(0.5)

        self.play(
            star.animate.scale(0.2),
            FadeOut(pressure_arrows),
            run_time=2
        )

        explosion = Circle(radius=0.3, color=ORANGE)
        self.play(FadeIn(explosion))
        self.play(
            explosion.animate.scale(10).set_opacity(0),
            run_time=2
        )

        self.wait(1)
        