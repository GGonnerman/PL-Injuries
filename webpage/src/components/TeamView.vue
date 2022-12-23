<template>
    <div class="team" @click="expanded = !expanded">
        <h4 class="team_name">
            {{ capitalize(team.team_name) }} (<span
                :style="{ color: get_color(team.players.length) }"
                >{{ team.players.length }}</span
            >)
        </h4>
        <collapse-transition>
            <div class="team_table_container" v-show="expanded">
                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Reason</th>
                            <th>Details</th>
                            <th>Potential Return</th>
                            <th>Condition</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="player in team.players" :key="player.name">
                            <td>{{ player.name }}</td>
                            <td>{{ player.reason }}</td>
                            <td>{{ player.details }}</td>
                            <td>{{ player.potential_return }}</td>
                            <td>{{ player.condition }}</td>
                            <td>{{ player.status }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </collapse-transition>
    </div>
</template>

<script>
import CollapseTransition from "@ivanv/vue-collapse-transition/src/CollapseTransition.vue";

export default {
    components: {
        CollapseTransition,
    },
    props: ["team"],
    data() {
        return {
            expanded: false,
            isOpen: false,
        };
    },
    methods: {
        capitalize(str) {
            return str.replaceAll("-", " ").split(" ").map(word => word[0].toUpperCase() + word.substr(1)).join(" ");
        },
        get_color(players_injured) {
            const hue = Math.min(players_injured / 11, 1) * -120 + 120;
            return "hsl(" + hue + ", 100%, 50%)";
        },
    },
};
</script>

<style>
.team {
    cursor: pointer;
}

@media screen and (max-width: 990px) {
    .team_table_container td {
        border-color: hsl(206, 29%, 25%) !important;
        color: hsl(206, 29%, 75%)
    }

    .team_table_container thead {
        visibility: hidden;
        height: 0;
        position: absolute;
        overflow: hidden;
    }

    .team_table_container tr {
        display: block;
        margin-bottom: 0.625em;
    }

    .team_table_container td:first-child {
        font-weight: bold;
        font-size: 18px;
        color: HSL(206, 29%, 84%);
    }

    .team_table_container td:nth-child(2)::before {
        content: "Reason: \00a0";
        text-transform: capitalize;
    }

    .team_table_container td:nth-child(3)::before {
        content: "Details: \00a0";
        text-transform: capitalize;
    }

    .team_table_container td:nth-child(4)::before {
        content: "Potential Return: \00a0";
        text-transform: capitalize;
    }

    .team_table_container td:nth-child(5)::before {
        content: "Condition: \00a0";
        text-transform: capitalize;
    }

    .team_table_container td:nth-child(6)::before {
        content: "Status: \00a0";
        text-transform: capitalize;
    }

    .team_table_container td {
        border-top: 1px solid;
        border-left: 5px solid;
        border-right: 5px solid;
        border-bottom: none;
        display: block;
        font-size: 0.85em;
        text-align: left;
    }

    .team_table_container td::before {
        content: attr(data-label);
        float: left;
        font-weight: bold;
        text-transform: uppercase;
    }

    .team_table_container td:first-child {
        border-top: 5px solid;
    }

    .team_table_container td:last-child {
        border-bottom: 5px solid;
    }
}
@media screen and (min-width: 991px) {
thead > tr > th {
    font-weight: bold;
}
tbody > tr > td:first-child {

    font-weight: bold;
}
}
</style>