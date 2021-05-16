<template>
    <router-link :to="address">
        <button>
            {{ text }}
        </button>
    </router-link>
</template>

<script>
export default {
    name: "LinkButton",
    
    props: {
        address: String,
        text: String,
    },
};
</script>

<style scoped>
button {
    margin-right: 20px;
}
</style>
