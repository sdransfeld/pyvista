"""
.. _antialiasing_example:

Anti-Aliasing
~~~~~~~~~~~~~

PyVista supports three types of anti-aliasing:

* ``"ssaa"`` - Super-Sample Anti-Aliasing
* ``"mxaa"`` - Multi-Sample Anti-Aliasing
* ``"fxaa"`` - Fast Approximate Anti-Aliasing

By default, anti-aliasing is disabled, but can be enabled globally with:

.. code:: python

   >>> import pyvista as pv
   >>> pv.global_theme.antialiasing = 'ssaa'

**Which Anti Aliasing Technique should You use?**

Those who have PCs with high-end configuration should opt for ``"ssaa"`` or
``"mxaa"``. Low-end PCs should use ``"fxaa"``.

"""

import pyvista as pv
from pyvista import examples

bunny = examples.download_bunny()

###############################################################################
# No Anti-Aliasing
# ~~~~~~~~~~~~~~~~
# First, let's show a plot without any anti-aliasing.

# obtained with `cpos = pl.show(return_cpos=True)`
cpos = [(-0.08566, 0.18735, 0.20116), (-0.05332, 0.12168, -0.01215), (-0.00151, 0.95566, -0.29446)]

pl = pv.Plotter()
pl.add_mesh(bunny, show_edges=True)
pl.disable_anti_aliasing()
pl.camera_position = cpos
pl.show()


###############################################################################
# Fast Approximate Anti-Aliasing (FXAA)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Also known as Fast Approximate Anti-Aliasing, FXAA was crafted by
# Nvidia. When it comes to anti-aliasing on low-end devices/PCs, FXAA is the
# best technique. It’s because, in terms of hardware or GPU, FXAA is not that
# demanding. It directly smoothens the 2D image as soon as it appears on the
# screen. This reduces the strain over GPU, making it best for low-end PCs.

pl = pv.Plotter()
pl.add_mesh(bunny, show_edges=True)
pl.enable_anti_aliasing('fxaa')
pl.camera_position = cpos
pl.show()


###############################################################################
# Multi-Sample Anti-Aliasing (MSAA)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MSAA, or Multi-Sample Anti-Aliasing is an optimization of SSAA that reduces
# the amount of pixel shader evaluations that need to be computed by focusing
# on overlapping regions of the scene. The result is antialiasing along edges
# that is on par with SSAA and less anti-aliasing along surfaces as these make
# up the bulk of SSAA computations. MSAA is substantially less computationally
# expensive than SSAA and results in comparable image quality.


pl = pv.Plotter()
pl.add_mesh(bunny, show_edges=True)
pl.enable_anti_aliasing('mxaa')
pl.camera_position = cpos
pl.show()


###############################################################################
# Super-Sample Anti-Aliasing (SSAA)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SSAA, or Super-Sample Anti-Aliasing is a brute force method of
# anti-aliasing. It results in the best image quality but comes at a tremendous
# resource cost. SSAA works by rendering the scene at a higher resolution. The
# final image is produced by downsampling the massive source image using an
# averaging filter. This acts as a low pass filter which removes the high
# frequency components that caused the jaggedness.

pl = pv.Plotter()
pl.add_mesh(bunny, show_edges=True, line_width=2)  # lines are thinner in SSAA
pl.enable_anti_aliasing('ssaa')
pl.camera_position = cpos
pl.show()