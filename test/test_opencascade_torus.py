#! /usr/bin/env python
# -*- coding: utf-8 -*-
from math import pi
import pygmsh
import pytest

from helpers import compute_volume


@pytest.mark.skipif(
    pygmsh.get_gmsh_major_version() < 3,
    reason='requires Gmsh >= 3'
    )
def test():
    geom = pygmsh.opencascade.Geometry()

    geom.add_torus([0.0, 0.0, 0.0], 1.0, 0.3, 1.25*pi, char_length=0.1)

    ref = 1.09994740709
    points, cells, _, _, _ = pygmsh.generate_mesh(geom)
    assert abs(compute_volume(points, cells) - ref) < 1.0e-2 * ref
    return points, cells


if __name__ == '__main__':
    import meshio
    meshio.write('opencascade_torus.vtu', *test())
