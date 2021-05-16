const state = {
    tickets: [],
    nextPage: "",
    prevPage: "",
};

const getters = {
    tickets: state => state.tickets,
    nextPage: state => state.nextPage,
    prevPage: state => state.prevPage,
};

const mutations = {
    setState: (state, {tickets, nextPage, prevPage}) => {
        state.tickets = tickets;
        state.nextPage = nextPage;
        state.prevPage = prevPage;
    },
};

const actions = {

    async getTicketList({ commit, rootGetters }, url) {
        const isAuth = rootGetters['authenticated'];
        
        if (!isAuth)
            return;

        const accessToken = rootGetters['accessToken'];

        const res = await fetch(url, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${accessToken}`
            },
        });

        if (res.status === 200) {
            const data = await res.json();
            commit("setState", 
                {tickets: data.result, 
                    nextPage: data.next, 
                    prevPage: data.previous});
        }
        else if (res.status === 401) {
            this.dispatch("setAuthFailed");
            throw "Invalid Access Token";
        }
        else
            throw "Error Getting Tickets";
    },


    async createTicket({ rootGetters }, ticket) {
        const isAuth = rootGetters['authenticated'];

        if(!isAuth)
            return;

        const accessToken = rootGetters['accessToken'];

        const res = await fetch("http://localhost:8000/ticket/", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${accessToken}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify(ticket),
        });
        
        if (res.status === 401) {
            this.dispatch("setAuthFailed");
            throw "Invalid Access Token";
        }
        else if (res.status !== 201) {
            const data = await res.json()
            throw `Error Creating Ticket. ${JSON.stringify(data)}`;
        }
    },


    async getTicket({ rootGetters }, id) {
        const isAuth = rootGetters['authenticated'];

        if(!isAuth)
            return;

        const accessToken = rootGetters['accessToken'];

        const res = await fetch(`http://localhost:8000/ticket/${id}/`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${accessToken}`
            },
        });
        
        if (res.status === 200) {
            const data = await res.json();
            return data;
        }
        else if (res.status === 401) {
            this.dispatch("setAuthFailed");
            throw "Invalid Access Token";
        }
        else
            throw "Error Getting Ticket";
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};