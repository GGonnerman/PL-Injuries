<template>
    <div class="container">
        <h1 class="title">PL Football Injuries</h1>
        <LeagueView />
        <p>All credit goes to <a href="https://www.premierinjuries.com/">Premier Injuries</a> for the original data.</p>
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
