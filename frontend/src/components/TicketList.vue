<template>
    <div v-if="!authenticated">
        <h3>You are logged out. Login to see the list.</h3>
    </div>
  
    <div v-if="!lastRequest.isSuccess" class="text-danger">
        {{ lastRequest.statusMsg }}
    </div>
  
    <div v-if="authenticated">

        <input type="text" placeholder="Category" v-model="category"/>
        <input type="text" placeholder="Impact" v-model="impact"/>
        <button @click="filterList" class="mb-4">Filter</button><br>

        <button @click="clickedPrevPage" class="mr-4 mb-4">Previous Page</button>
        <button @click="clickedNextPage">Next Page</button>
        
        <div v-for="ticket in tickets" 
            :key="ticket.id"
            class="bg-light text-black mb-4"
            data-toggle="modal" 
            :data-target="`#ticket-${ticket.id}`">
        
            <TicketModal :ticketId="ticket.id"/>
            
            <p>#{{ ticket.id }}</p>
            <h4 class="title"><b>{{ ticket.title }}</b></h4>
            <p>(Author: <b>{{ ticket.author }})</b></p>

            <div>
                <p>Impact: <b>{{ ticket.impact }}</b></p>

                <div class="float-right">
                    <p v-if="ticket.assignee">
                        Assigned to User: <b>{{ ticket.assignee }}</b>
                    </p><br>
                    <p v-if="ticket.group">
                        Assigned to Group: <b>{{ ticket.group }}</b>
                    </p>
                </div>

                <br>
                <p v-if="ticket.category">Category: <b>{{ ticket.category }}</b></p>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex"

import TicketModal from "./TicketModal"

export default {
    name: 'TicketList',

    data() {
        return {
            lastRequest: {
                isSuccess: true,
                statusMsg: "",
            },
            url: "http://localhost:8000/ticket/",
            category: "",
            impact: "",
        }
    },

    methods: {
        ...mapActions(["getTicketList"]),

        async getAllTickets() {
            try {
                await this.getTicketList(this.url);
                this.lastRequest.isSuccess = true;
                this.lastRequest.statusMsg = "Success";
            }
            catch(e) {
                this.lastRequest.isSuccess = false;
                this.lastRequest.statusMsg = String(e);
            }
        },

        clickedNextPage() {
            if (this.nextPage) {
                this.url = this.nextPage;
                this.getAllTickets();
            }
        },

        clickedPrevPage() {
            if (this.prevPage) {
                this.url = this.prevPage;
                this.getAllTickets();
            }
        },

        filterList() {
            let api_url = this.url.split("?")[0];
            this.url = `${api_url}?page=1`;

            if (this.category)
                this.url = `${this.url}&category=${this.category}`;

            if (this.impact)
                this.url = `${this.url}&impact=${this.impact}`;

            this.getAllTickets();
        }
    },

    created() {
        this.getAllTickets();
    },

    computed: {
        ...mapGetters(["tickets", "nextPage", "prevPage", "authenticated"]),
    },

    components: {
        TicketModal,
    }
};
</script>

<style scoped>
p, h4.title  {
  display: inline;
  margin-right: 40px;
}

.float-right {
  float: right;
  margin-right: 20px;
}
</style>
