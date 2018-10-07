import os
import socket

g_render4cnn_root_folder = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------
# PATHS
# ------------------------------------------------------------
g_blender_executable_path = '/Applications/Blender/blender.app/Contents/MacOS/blender' #!! MODIFY if necessary
g_matlab_executable_path = '/Applications/MATLAB_R2017b.app/Contents/MacOS/MATLAB' # !! MODIFY if necessary
g_blank_blend_file_path = os.path.join(g_render4cnn_root_folder, 'supplementary/blank.blend')


# ------------------------------------------------------------
# render_model_views
# ------------------------------------------------------------
g_syn_light_num_lowbound = 0
g_syn_light_num_highbound = 6
g_syn_light_dist_lowbound = 8
g_syn_light_dist_highbound = 20
g_syn_light_azimuth_degree_lowbound = 0
g_syn_light_azimuth_degree_highbound = 360
g_syn_light_elevation_degree_lowbound = -90
g_syn_light_elevation_degree_highbound = 90
g_syn_light_energy_mean = 2
g_syn_light_energy_std = 2
g_syn_light_environment_energy_lowbound = 0
g_syn_light_environment_energy_highbound = 1