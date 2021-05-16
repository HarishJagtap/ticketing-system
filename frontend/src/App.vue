<template>
    <h1 class="outer">Ticketing System</h1>

    <div class="outer">
        <LinkButton address="/" text="List all tickets"/>
        <LinkButton address="/create" text="Create new ticket"/>
        <LinkButton address="/login" text="Login"/>
    </div>
    
    <div class="outer">
        <router-view/>
    </div>
</template>

<script>
import LinkButton from "./components/LinkButton"

export default {
    name: "App",
    
    components: {
        LinkButton
    },
};
</script>

<style>
.outer {
    margin: 30px;
}
</style>
