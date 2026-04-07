import schemdraw
import schemdraw.logic as logic

with schemdraw.Drawing() as d:
    and_gate = d.add(logic.And(inputs=2).color("blue"))
    or_gate = d.add(logic.Or().right().at(and_gate.out).color("green"))
    not_gate = d.add(logic.Not().right().at(or_gate.out).color("red"))

    d.draw()