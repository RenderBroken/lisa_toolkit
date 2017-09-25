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
    ( 300000, ActiveState(capacity=149, power=90)),
    ( 364800, ActiveState(capacity=180, power=110)),
    ( 441600, ActiveState(capacity=211, power=130)),
    ( 518400, ActiveState(capacity=242, power=150)),
    ( 595200, ActiveState(capacity=273, power=175)),
    ( 672000, ActiveState(capacity=304, power=195)),
    ( 748800, ActiveState(capacity=335, power=220)),
    ( 825600, ActiveState(capacity=366, power=245)),
    ( 883200, ActiveState(capacity=397, power=275)),
    ( 960000, ActiveState(capacity=428, power=305)),
    (1036800, ActiveState(capacity=459, power=340)),
    (1094400, ActiveState(capacity=490, power=370)),
    (1171200, ActiveState(capacity=521, power=410)),
    (1248000, ActiveState(capacity=552, power=460)),
    (1324800, ActiveState(capacity=583, power=490)),
    (1401600, ActiveState(capacity=614, power=540)),
    (1478400, ActiveState(capacity=645, power=590)),
    (1555200, ActiveState(capacity=676, power=650)),
    (1670400, ActiveState(capacity=707, power=700)),
    (1747200, ActiveState(capacity=738, power=760)),
    (1824000, ActiveState(capacity=769, power=840)),
    (1900800, ActiveState(capacity=800, power=910)),
])

silver_cluster_active_states = OrderedDict([
    ( 300000, ActiveState(power=4)),
    ( 364800, ActiveState(power=4)),
    ( 441600, ActiveState(power=4)),
    ( 518400, ActiveState(power=4)),
    ( 595200, ActiveState(power=4)),
    ( 672000, ActiveState(power=4)),
    ( 748800, ActiveState(power=8)),
    ( 825600, ActiveState(power=9)),
    ( 883200, ActiveState(power=15)),
    ( 960000, ActiveState(power=16)),
    (1036800, ActiveState(power=21)),
    (1094400, ActiveState(power=22)),
    (1171200, ActiveState(power=29)),
    (1248000, ActiveState(power=32)),
    (1324800, ActiveState(power=41)),
    (1401600, ActiveState(power=45)),
    (1478400, ActiveState(power=49)),
    (1555200, ActiveState(power=52)),
    (1670400, ActiveState(power=56)),
    (1747200, ActiveState(power=62)),
    (1824000, ActiveState(power=69)),
    (1900800, ActiveState(power=75)),
])

gold_cpu_active_states = OrderedDict([
    ( 300000, ActiveState(capacity=149, power=90)),
    ( 345600, ActiveState(capacity=180, power=110)),
    ( 422400, ActiveState(capacity=211, power=130)),
    ( 499200, ActiveState(capacity=242, power=150)),
    ( 576000, ActiveState(capacity=273, power=175)),
    ( 652800, ActiveState(capacity=304, power=195)),
    ( 729600, ActiveState(capacity=335, power=220)),
    ( 806400, ActiveState(capacity=366, power=245)),
    ( 902400, ActiveState(capacity=397, power=275)),
    ( 979200, ActiveState(capacity=428, power=305)),
    (1056000, ActiveState(capacity=459, power=340)),
    (1132800, ActiveState(capacity=490, power=370)),
    (1190400, ActiveState(capacity=521, power=410)),
    (1267200, ActiveState(capacity=552, power=460)),
    (1344000, ActiveState(capacity=583, power=490)),
    (1420800, ActiveState(capacity=614, power=540)),
    (1497600, ActiveState(capacity=645, power=590)),
    (1574400, ActiveState(capacity=676, power=650)),
    (1651200, ActiveState(capacity=707, power=700)),
    (1728000, ActiveState(capacity=738, power=760)),
    (1804800, ActiveState(capacity=769, power=840)),
    (1881600, ActiveState(capacity=800, power=910)),
    (1958400, ActiveState(capacity=825, power=980)),
    (2035200, ActiveState(capacity=850, power=1045)),
    (2112000, ActiveState(capacity=870, power=1100)),
    (2208000, ActiveState(capacity=890, power=1160)),
    (2265600, ActiveState(capacity=910, power=1215)),
    (2323200, ActiveState(capacity=932, power=1280)),
    (2342400, ActiveState(capacity=961, power=1380)),
    (2361600, ActiveState(capacity=990, power=1500)),
    (2457600, ActiveState(capacity=1024, power=1715)),
])

gold_cluster_active_states = OrderedDict([
    ( 300000, ActiveState(power=4)),
    ( 345600, ActiveState(power=4)),
    ( 422400, ActiveState(power=4)),
    ( 499200, ActiveState(power=4)),
    ( 576000, ActiveState(power=4)),
    ( 652800, ActiveState(power=4)),
    ( 729600, ActiveState(power=8)),
    ( 806400, ActiveState(power=9)),
    ( 902400, ActiveState(power=15)),
    ( 979200, ActiveState(power=16)),
    (1056000, ActiveState(power=21)),
    (1132800, ActiveState(power=22)),
    (1190400, ActiveState(power=29)),
    (1267200, ActiveState(power=32)),
    (1344000, ActiveState(power=41)),
    (1420800, ActiveState(power=45)),
    (1497600, ActiveState(power=49)),
    (1574400, ActiveState(power=52)),
    (1651200, ActiveState(power=56)),
    (1728000, ActiveState(power=62)),
    (1804800, ActiveState(power=69)),
    (1881600, ActiveState(power=75)),
    (1958400, ActiveState(power=81)),
    (2035200, ActiveState(power=90)),
    (2112000, ActiveState(power=93)),
    (2208000, ActiveState(power=97)),
    (2265600, ActiveState(power=104)),
    (2323200, ActiveState(power=109)),
    (2342400, ActiveState(power=115)),
    (2361600, ActiveState(power=123)),
    (2457600, ActiveState(power=131)),
])

# TODO warn if any of the idle states aren't represented by power domains
cpu_idle_states = OrderedDict([
    ("WFI",               0),
    ("cpu-sleep-0",       0),
    ("cluster-sleep-0",   0),
])

cluster_idle_states = OrderedDict([
    ("WFI",               0),
    ("cpu-sleep-0",       0),
    ("cluster-sleep-0",   0),
])

silvers = [0, 1, 2, 3]
golds = [4, 5, 6, 7]

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

op5_energy = EnergyModel(
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
