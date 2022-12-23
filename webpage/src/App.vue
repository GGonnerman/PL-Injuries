<template>
    <div class="container">
        <h1 class="title">Premier League Injuries</h1>
        <LeagueView />
    </div>
</template>

<script>
import LeagueView from "./components/LeagueView.vue";

export default {
    name: "App",
    components: {
        LeagueView,
    },
};
</script>

<style>
#app {
  font-size: 22px;
}
.title {
  margin: 30px 0px;
}

</style>
