# SPDX-License-Identifier: Apache-2.0
#
# Copyright (C) 2016, ARM Limited and contributors.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from energy_model import (ActiveState, EnergyModelNode, EnergyModelRoot,
                          PowerDomain, EnergyModel)

from collections import OrderedDict

silver_cpu_active_states = OrderedDict([
    ( 307200, ActiveState(capacity=149, power=90)),
    ( 422400, ActiveState(capacity=205, power=121)),
    ( 480000, ActiveState(capacity=229, power=142)),
    ( 556800, ActiveState(capacity=253, power=164)),
    ( 652800, ActiveState(capacity=296, power=198)),
    ( 729600, ActiveState(capacity=350, power=239)),
    ( 844800, ActiveState(capacity=406, power=306)),
    ( 960000, ActiveState(capacity=460, power=371)),
    (1036800, ActiveState(capacity=491, power=430)),
    (1113600, ActiveState(capacity=527, power=486)),
    (1190400, ActiveState(capacity=572, power=541)),
    (1228800, ActiveState(capacity=584, power=586)),
    (1324800, ActiveState(capacity=630, power=651)),
    (1401600, ActiveState(capacity=666, power=732)),
    (1478400, ActiveState(capacity=711, power=827)),
    (1593600, ActiveState(capacity=763, power=925)),
])

silver_cluster_active_states = OrderedDict([
    ( 307200, ActiveState(power=4)),
    ( 422400, ActiveState(power=4)),
    ( 480000, ActiveState(power=4)),
    ( 556800, ActiveState(power=4)),
    ( 652800, ActiveState(power=4)),
    ( 729600, ActiveState(power=8)),
    ( 844800, ActiveState(power=9)),
    ( 960000, ActiveState(power=16)),
    (1036800, ActiveState(power=21)),
    (1113600, ActiveState(power=22)),
    (1190400, ActiveState(power=29)),
    (1228800, ActiveState(power=32)),
    (1324800, ActiveState(power=41)),
    (1401600, ActiveState(power=42)),
    (1478400, ActiveState(power=49)),
    (1593600, ActiveState(power=52)),
])

gold_cpu_active_states = OrderedDict([
    ( 307200, ActiveState(capacity=149, power=93)),
    ( 403200, ActiveState(capacity=197, power=116)),
    ( 480000, ActiveState(capacity=229, power=142)),
    ( 556800, ActiveState(capacity=253, power=164)),
    ( 652800, ActiveState(capacity=296, power=198)),
    ( 729600, ActiveState(capacity=350, power=239)),
    ( 806400, ActiveState(capacity=372, power=270)),
    ( 883200, ActiveState(capacity=400, power=310)),
    ( 940800, ActiveState(capacity=445, power=345)),
    (1036800, ActiveState(capacity=495, power=400)),
    (1113600, ActiveState(capacity=527, power=486)),
    (1190400, ActiveState(capacity=572, power=541)),
    (1248000, ActiveState(capacity=598, power=567)),
    (1324800, ActiveState(capacity=630, power=651)),
    (1401600, ActiveState(capacity=666, power=732)),
    (1478400, ActiveState(capacity=711, power=827)),
    (1555200, ActiveState(capacity=743, power=865)),
    (1632000, ActiveState(capacity=780, power=946)),
    (1708800, ActiveState(capacity=812, power=1040)),
    (1785600, ActiveState(capacity=850, power=1097)),
    (1824000, ActiveState(capacity=868, power=1209)),
    (1920000, ActiveState(capacity=914, power=1311)),
    (1996800, ActiveState(capacity=961, power=1441)),
    (2073600, ActiveState(capacity=988, power=1535)),
    (2150400, ActiveState(capacity=1024, power=1715)),
])

gold_cluster_active_states = OrderedDict([
    ( 307200, ActiveState(power=4)),
    ( 403200, ActiveState(power=4)),
    ( 480000, ActiveState(power=4)),
    ( 556800, ActiveState(power=4)),
    ( 652800, ActiveState(power=4)),
    ( 729600, ActiveState(power=4)),
    ( 806400, ActiveState(power=7)),
    ( 883200, ActiveState(power=10)),
    ( 940800, ActiveState(power=15)),
    (1036800, ActiveState(power=16)),
    (1113600, ActiveState(power=21)),
    (1190400, ActiveState(power=22)),
    (1248000, ActiveState(power=29)),
    (1324800, ActiveState(power=32)),
    (1401600, ActiveState(power=41)),
    (1478400, ActiveState(power=42)),
    (1555200, ActiveState(power=49)),
    (1632000, ActiveState(power=52)),
    (1708800, ActiveState(power=62)),
    (1785600, ActiveState(power=69)),
    (1824000, ActiveState(power=75)),
    (1920000, ActiveState(power=81)),
    (1996800, ActiveState(power=90)),
    (2073600, ActiveState(power=93)),
    (2150400, ActiveState(power=96)),
])

# TODO warn if any of the idle states aren't represented by power domains
cpu_idle_states = OrderedDict([
    ("WFI",               2),
    ("cpu-sleep-0",       0),
    ("cluster-sleep-0",   0),
])

cluster_idle_states = OrderedDict([
    ("WFI",               0),
    ("cpu-sleep-0",       0),
    ("cluster-sleep-0",   0),
])

silvers = [0, 1]
golds = [2, 3]

def silver_cpu_node(cpu):
    return EnergyModelNode(cpu=cpu,
                           active_states=silver_cpu_active_states,
                           idle_states=cpu_idle_states)

def gold_cpu_node(cpu):
    return EnergyModelNode(cpu=cpu,
                           active_states=gold_cpu_active_states,
                           idle_states=cpu_idle_states)

def cpu_pd(cpu):
    return PowerDomain(cpu=cpu, idle_states=["WFI", "cpu-sleep-0"])

op3_energy = EnergyModel(
    root_node=EnergyModelRoot(children=[
        EnergyModelNode(name='cluster_silver',
                        children=[silver_cpu_node(c) for c in silvers],
                        active_states=silver_cluster_active_states,
                        idle_states=cluster_idle_states),
        EnergyModelNode(name='cluster_gold',
                        children=[gold_cpu_node(c) for c in golds],
                        active_states=gold_cluster_active_states,
                        idle_states=cluster_idle_states)]),
    root_power_domain=PowerDomain(idle_states=[], children=[
        PowerDomain(idle_states=['cluster-sleep-0'], children=[
            cpu_pd(c) for c in silvers]),
        PowerDomain(idle_states=['cluster-sleep-0'], children=[
            cpu_pd(c) for c in golds])]),
    freq_domains=[silvers, golds])
