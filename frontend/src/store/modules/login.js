const state = {
    accessToken: "",
    authenticated: false,
};

const getters = {
    accessToken: state => state.accessToken,
    authenticated: state => state.authenticated,
};

const mutations = {
    setAccessToken: (state, accessToken) => state.accessToken = accessToken,
    setAuthenticated: (state, authenticated) => state.authenticated = authenticated,
};

const actions = {

    async login({ commit }, { username, password }) {

        const res = await fetch("http://localhost:8000/login/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        if (res.status === 201) {
            const data = await res.json();
            commit("setAccessToken", data.access_token);
            commit("setAuthenticated", true);
        }
        else if (res.status === 403) {
            commit("setAuthenticated", false);
            throw "Incorrect Password";
        }
        else
            throw "Error Logging In";
    },


    setAuthFailed({ commit }) {
        commit("setAuthenticated", false);
    }
};

export default {
    state,
    getters,
    mutations,
    actions,
};