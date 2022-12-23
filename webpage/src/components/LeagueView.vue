<template>
    <TeamView v-for="team in get_team_data" :team="team" :key="team.name"/>
</template>

<script>
import TeamView from "./TeamView.vue";
import team_data from "../team_data.json";

const x = team_data[0];
console.log(x);

export default {
    data() {
        return team_data;
    },
    components: {
        TeamView,
    },
    computed: {
        get_team_data() {
            return team_data;
        }
    }
 //   components: {
 //       TeamView,
 //   },
};
</script>

<style>
</style>