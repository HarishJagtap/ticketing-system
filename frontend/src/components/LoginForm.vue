<template>
    <div v-if="!loginStatus.isSuccess" class="text-danger">
        Failed to Login. {{ loginStatus.msg }}
    </div>

    <div v-if="authenticated" class="text-success">
        Logged in successfully.
    </div>

    <form @submit="onSubmit">
        <label for="username">Username:</label><br>
        <input type="text"
            id="username"
            v-model="username"/><br>

        <label for="password">Password:</label><br>
        <input type="password"
            id="password"
            v-model="password"/><br>
        
        <br>
        <input type="submit" value="Login"/>
    </form>
</template>

<script>
import { mapGetters, mapActions } from "vuex"

export default {
    name: 'LoginForm',

    data() {
        return {
            username: "",
            password: "",
            loginStatus: {
                isSuccess: true,
                msg: "",
            },
        }
    },

    computed: {
        ...mapGetters(["accessToken", "authenticated"]),
    },

    methods: {
        ...mapActions(["login"]),
        
        async onSubmit(e) {
            e.preventDefault();

            if (!this.username || !this.password)
                return;

            try {
                await this.login({ username: this.username, password: this.password });
                this.loginStatus.isSuccess = true;
            }
            catch(e) {
                this.loginStatus.isSuccess = false;
                this.loginStatus.msg = String(e);
            }
        }
    },
};
</script>