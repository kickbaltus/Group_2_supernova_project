from manim import *
import numpy as np

class supernovaintro(Scene):
    def construct(self):

        text = Text("Our research about the crab nebula")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

        ster = Circle(radius=2, color=YELLOW)
        self.play(Create(ster))
        self.wait(0.5)

        text = Text("What is a supernova?").scale(0.5)
        text.next_to(ster, UP, buff=0.3)

        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        
        pijlen_out = VGroup()

        for i in range(8):

            angle = i / 8
            start_point = ster.point_from_proportion(angle)

            direction = normalize(start_point)

            arrow = Arrow(
                start=start_point,
                end=start_point + direction * 1,
                buff=0,
                color=RED
            )

            pijlen_out.add(arrow)

        self.play(Create(pijlen_out))
        self.wait(1)

        pijlen_in = VGroup()

        for i in range(8):

            angle = i / 8
            start_point = ster.point_from_proportion(angle)

            direction = normalize(start_point)

            arrow = Arrow(
                start=start_point,             
                end=start_point - direction * 1,
                buff=0,
                color=BLUE
            )

            pijlen_in.add(arrow)

        self.play(Create(pijlen_in))
        self.wait(1)
        
        self.play(FadeOut(pijlen_out))
        self.wait(0.5)
        
        self.play(
            ster.animate.scale(0.01),
            FadeOut(pijlen_in),
            run_time=2
            )

        explosie = Circle(radius=0.01, color=RED)
        self.play(
            explosie.animate.scale((350)).set_opacity(1) )
        self.wait(2)
        self.play(FadeOut(explosie))
        self.play(FadeOut(ster))
        self.wait(2)
        
        foto = ImageMobject("telescope.webp")
        foto.scale(1)  
        self.add(foto)
        self.wait(2)
        self.play(FadeOut(foto))
        
        foto = ImageMobject("narrowband.webp")
        foto.scale(1.7)  
        self.add(foto)
        self.wait(4)
        
        pijlo = Arrow(
            start=[-0.7, 3.0, 0],
            end=[-0.7, 2.5, 0],
            buff=0
        )
        pijlH = Arrow(
            start=[1.4, 3.0, 0],
            end=[1.4, 2.5, 0],
            buff=0
        )
        
        pijlS = Arrow(
            start=[1.9, 3.0, 0],
            end=[1.9, 2.5, 0],
            buff=0
        )
        
        self.play(Write(pijlo))
        self.play(Write(pijlH))
        self.play(Write(pijlS))        
        self.wait(3)
        
        self.play(FadeOut(pijlo), FadeOut(pijlH), FadeOut(pijlS), FadeOut(foto))
        
        LABEL_Y = UP * 2

        # Images
        s = ImageMobject("03_SII_distribution.png").scale(0.2)
        h = ImageMobject("01_Ha_distribution.png").scale(0.2)
        o = ImageMobject("02_OIII_distribution.png").scale(0.2)

        sho = ImageMobject("04_SHO_distribution.png").scale(0.2)

        S_H = ImageMobject("SII_Ha_heatmap.png").scale(0.18)

        LABEL_Y = UP * 2

        s_label = Text("SII").scale(0.5)
        h_label = Text("Hα").scale(0.5)
        o_label = Text("OIII").scale(0.5)

        sho_label = Text("Hα + SII + OIII").scale(0.6)
        S_H_label = Text("SII/Hα").scale(0.6)

        s.move_to(LEFT * 4)
        h.move_to(ORIGIN)
        o.move_to(RIGHT * 4)

        s_label.move_to(s.get_center() + LABEL_Y)
        h_label.move_to(h.get_center() + LABEL_Y)
        o_label.move_to(o.get_center() + LABEL_Y)


        self.play(FadeIn(s), FadeIn(s_label))
        self.wait(0.5)

        self.play(FadeIn(h), FadeIn(h_label))
        self.wait(0.5)

        self.play(FadeIn(o), FadeIn(o_label))
        self.wait(2)

        self.play(
            s.animate.move_to(ORIGIN),
            h.animate.move_to(ORIGIN),
            o.animate.move_to(ORIGIN),

            s_label.animate.move_to(ORIGIN + LABEL_Y),
            h_label.animate.move_to(ORIGIN + LABEL_Y),
            o_label.animate.move_to(ORIGIN + LABEL_Y),

            run_time=1.5
        )

        sho_label.move_to(sho.get_center() + LABEL_Y)
        self.play(FadeOut(s_label), FadeOut(h_label), FadeOut(o_label))
        self.play(FadeIn(sho), FadeIn(sho_label))
        self.wait(5)

        self.play(FadeOut(sho), FadeOut(sho_label))

        s_target = LEFT * 4
        h_target = ORIGIN
        o_target = RIGHT * 4

        # animatie
        self.play(
            s.animate.move_to(s_target),
            h.animate.move_to(h_target),
            o.animate.move_to(o_target),

            s_label.animate.move_to(s_target + LABEL_Y),
            h_label.animate.move_to(h_target + LABEL_Y),
            o_label.animate.move_to(o_target + LABEL_Y),

            run_time=1.5
        )

        self.wait(5)

        self.play(FadeOut(o), FadeOut(o_label))

        self.play(
            s.animate.move_to(ORIGIN),
            h.animate.move_to(ORIGIN),

            s_label.animate.move_to(ORIGIN + LABEL_Y),
            h_label.animate.move_to(ORIGIN + LABEL_Y),

            run_time=1.5
        )

        self.play(FadeOut(s_label), FadeOut(h_label))
        S_H_label.move_to(S_H.get_center() + LABEL_Y)

        self.play(FadeIn(S_H), FadeIn(S_H_label))
        self.wait(8)

        self.play(FadeOut(S_H), FadeOut(S_H_label))
        self.play(FadeIn(s_label), FadeIn(h_label))
        
        self.play(
            s.animate.move_to(s_target),
            h.animate.move_to(h_target),

            s_label.animate.move_to(s_target + LABEL_Y),
            h_label.animate.move_to(h_target + LABEL_Y),

            run_time=1.5
        )
        
        o.move_to(o_target)
        o_label.move_to(o_target + LABEL_Y)

        self.play(
            FadeIn(o),
            FadeIn(o_label))
        
        self.play(FadeOut(s), FadeOut(s_label))

        self.play(
            o.animate.move_to(ORIGIN),
            h.animate.move_to(ORIGIN),

            o_label.animate.move_to(ORIGIN + LABEL_Y),
            h_label.animate.move_to(ORIGIN + LABEL_Y),

            run_time=1.5
        )

        OH_heat = ImageMobject("OIII_Ha_heatmap.png").scale(0.18)
        OH_label = Text("OIII/Hα").scale(0.6)

        self.play(FadeOut(o_label), FadeOut(h_label))

        OH_label.move_to(OH_heat.get_center() + LABEL_Y)

        self.play(FadeIn(OH_heat), FadeIn(OH_label))
        self.wait(8)

        self.play(FadeOut(OH_heat), FadeOut(OH_label))

        self.play(FadeIn(o_label), FadeIn(h_label))

        self.play(
            o.animate.move_to(o_target),
            h.animate.move_to(h_target),

            o_label.animate.move_to(o_target + LABEL_Y),
            h_label.animate.move_to(h_target + LABEL_Y),

            run_time=1.5
        )

        self.play(FadeOut(h), FadeOut(h_label))

        self.play(
            o.animate.move_to(ORIGIN),
            s.animate.move_to(ORIGIN),

            o_label.animate.move_to(ORIGIN + LABEL_Y),
            s_label.animate.move_to(ORIGIN + LABEL_Y),

            run_time=1.5
        )

        OS_heat = ImageMobject("OIII_SII_heatmap.png").scale(0.18)
        OS_label = Text("OIII/SII").scale(0.6)

        self.play(FadeOut(o_label), FadeOut(s_label))

        OS_label.move_to(OS_heat.get_center() + LABEL_Y)

        self.play(FadeIn(OS_heat), FadeIn(OS_label))
        self.wait(8)

        self.play(FadeOut(OS_heat), FadeOut(OS_label))

        self.play(FadeIn(o_label), FadeIn(s_label))

        self.play(
            o.animate.move_to(o_target),
            s.animate.move_to(s_target),

            o_label.animate.move_to(o_target + LABEL_Y),
            s_label.animate.move_to(s_target + LABEL_Y),

            run_time=1.5
        )
        
        h.move_to(h_target + LABEL_Y)
        self.play(FadeIn(h), FadeIn(h_label))

        # alles naar midden
        self.play(
            s.animate.move_to(ORIGIN),
            h.animate.move_to(ORIGIN),
            o.animate.move_to(ORIGIN),

            s_label.animate.move_to(ORIGIN + LABEL_Y),
            h_label.animate.move_to(ORIGIN + LABEL_Y),
            o_label.animate.move_to(ORIGIN + LABEL_Y),

            run_time=1.5
        )

        self.wait(1)
        self.play(FadeOut(s_label), FadeOut(h_label), FadeOut(o_label))

        # SHO eroverheen
        sho.move_to(ORIGIN)
        sho_label.move_to(ORIGIN + LABEL_Y)

        self.play(FadeIn(sho), FadeIn(sho_label))
        self.wait(5)

        # fade alles uit (eindbeeld)
        self.play(
            FadeOut(sho),
            FadeOut(sho_label),
            FadeOut(s), FadeOut(h), FadeOut(o),
            FadeOut(s_label), FadeOut(h_label), FadeOut(o_label)
        )
        
        
        
        
        
        
        
        