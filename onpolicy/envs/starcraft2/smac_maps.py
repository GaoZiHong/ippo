from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pysc2.maps import lib


class SMACMap(lib.Map):
    directory = "SMAC_Maps"
    download = "https://github.com/oxwhirl/smac#smac-maps"
    players = 2
    step_mul = 8
    game_steps_per_episode = 0


map_param_registry = {
    "3m": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 60,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "8m": {
        "n_agents": 8,
        "n_enemies": 8,
        "limit": 120,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "25m": {
        "n_agents": 25,
        "n_enemies": 25,
        "limit": 150,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "5m_vs_6m": {
        "n_agents": 5,
        "n_enemies": 6,
        "limit": 70,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "8m_vs_9m": {
        "n_agents": 8,
        "n_enemies": 9,
        "limit": 120,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "10m_vs_11m": {
        "n_agents": 10,
        "n_enemies": 11,
        "limit": 150,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "27m_vs_30m": {
        "n_agents": 27,
        "n_enemies": 30,
        "limit": 180,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "MMM": {
        "n_agents": 10,
        "n_enemies": 10,
        "limit": 150,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 3,
        "map_type": "MMM",
    },
    "MMM2": {
        "n_agents": 10,
        "n_enemies": 12,
        "limit": 180,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 3,
        "map_type": "MMM",
    },
    "2s3z": {
        "n_agents": 5,
        "n_enemies": 5,
        "limit": 120,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
    },
    "3s5z": {
        "n_agents": 8,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
    },
    "3s5z_vs_3s6z": {
        "n_agents": 8,
        "n_enemies": 9,
        "limit": 170,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
    },
    "3s_vs_3z": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 150,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "stalkers",
    },
    "3s_vs_4z": {
        "n_agents": 3,
        "n_enemies": 4,
        "limit": 200,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "stalkers",
    },
    "3s_vs_5z": {
        "n_agents": 3,
        "n_enemies": 5,
        "limit": 250,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "stalkers",
    },
    "1c3s5z": {
        "n_agents": 9,
        "n_enemies": 9,
        "limit": 180,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 3,
        "map_type": "colossi_stalkers_zealots",
    },
    "2m_vs_1z": {
        "n_agents": 2,
        "n_enemies": 1,
        "limit": 150,
        "a_race": "T",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "corridor": {
        "n_agents": 6,
        "n_enemies": 24,
        "limit": 400,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "zealots",
    },
    "6h_vs_8z": {
        "n_agents": 6,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "Z",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "hydralisks",
    },
    "2s_vs_1sc": {
        "n_agents": 2,
        "n_enemies": 1,
        "limit": 300,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "stalkers",
    },
    "so_many_baneling": {
        "n_agents": 7,
        "n_enemies": 32,
        "limit": 100,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "zealots",
    },
    "bane_vs_bane": {
        "n_agents": 24,
        "n_enemies": 24,
        "limit": 200,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "bane",
    },
    "2c_vs_64zg": {
        "n_agents": 2,
        "n_enemies": 64,
        "limit": 400,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "colossus",
    },

    # This is adhoc environment
    "1c2z_vs_1c1s1z": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 180,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 3,
        "map_type": "colossi_stalkers_zealots",
    },
    "1c2s_vs_1c1s1z": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 180,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 3,
        "map_type": "colossi_stalkers_zealots",
    },
    "2c1z_vs_1c1s1z": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 180,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 3,
        "map_type": "colossi_stalkers_zealots",
    },
    "2c1s_vs_1c1s1z": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 180,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 3,
        "map_type": "colossi_stalkers_zealots",
    },
    "1c1s1z_vs_1c1s1z": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 180,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 3,
        "map_type": "colossi_stalkers_zealots",
    },

    "3s5z_vs_4s4z": {
        "n_agents": 8,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
    },
    "4s4z_vs_4s4z": {
        "n_agents": 8,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
    },
    "5s3z_vs_4s4z": {
        "n_agents": 8,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
    },
    "6s2z_vs_4s4z": {
        "n_agents": 8,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
    },
    "2s6z_vs_4s4z": {
        "n_agents": 8,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
    },

    "6m_vs_6m_tz": {
        "n_agents": 6,
        "n_enemies": 6,
        "limit": 70,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "5m_vs_6m_tz": {
        "n_agents": 5,
        "n_enemies": 6,
        "limit": 70,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "3s6z_vs_3s6z": {
        "n_agents": 9,
        "n_enemies": 9,
        "limit": 170,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
    },
    "7h_vs_8z": {
        "n_agents": 7,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "Z",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "hydralisks",
    },
    "2s2z_vs_zg": {
        "n_agents": 4,
        "n_enemies": 20,
        "limit": 200,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots_vs_zergling",
    },
    "1s3z_vs_zg": {
        "n_agents": 4,
        "n_enemies": 20,
        "limit": 200,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots_vs_zergling",
    },
    "3s1z_vs_zg": {
        "n_agents": 4,
        "n_enemies": 20,
        "limit": 200,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots_vs_zergling",
    },

    "2s2z_vs_zg_easy": {
        "n_agents": 4,
        "n_enemies": 18,
        "limit": 200,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots_vs_zergling",
    },
    "1s3z_vs_zg_easy": {
        "n_agents": 4,
        "n_enemies": 18,
        "limit": 200,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots_vs_zergling",
    },
    "3s1z_vs_zg_easy": {
        "n_agents": 4,
        "n_enemies": 18,
        "limit": 200,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots_vs_zergling",
    },
    "28m_vs_30m": {
        "n_agents": 28,
        "n_enemies": 30,
        "limit": 180,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "29m_vs_30m": {
        "n_agents": 29,
        "n_enemies": 30,
        "limit": 180,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "30m_vs_30m": {
        "n_agents": 30,
        "n_enemies": 30,
        "limit": 180,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "MMM2_test": {
        "n_agents": 10,
        "n_enemies": 12,
        "limit": 180,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 3,
        "map_type": "MMM",
    },
    # this is communication map
    "1o_10b_vs_1r": {
        "n_agents": 11,
        "n_enemies": 1,
        "limit": 50,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "overload_bane"
    },
    "1o_2r_vs_4r": {
        "n_agents": 3,
        "n_enemies": 4,
        "limit": 50,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "overload_roach"
    },
    "bane_vs_hM": {
        "n_agents": 3,
        "n_enemies": 2,
        "limit": 30,
        "a_race": "Z",
        "b_race": "T",
        "unit_type_bits": 2,
        "map_type": "bZ_hM"
    }
}


def get_smac_map_registry():
    return map_param_registry


for name in map_param_registry.keys():
    globals()[name] = type(name, (SMACMap,), dict(filename=name))


def get_map_params(map_name):
    map_param_registry = get_smac_map_registry()
    return map_param_registry[map_name]
