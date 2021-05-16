import { createStore } from 'vuex'

import login from "./modules/login"
import ticket from "./modules/ticket"

const store = createStore({
    modules: {
        login,
        ticket,
    },
});

export default store;
