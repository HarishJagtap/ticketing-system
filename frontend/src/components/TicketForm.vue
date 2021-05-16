<template>
    <div v-if="!authenticated">
        <h3>You are logged out. Login to create ticket.</h3>
    </div>

    <div :class="lastForm.isSuccess ? 'text-success' : 'text-danger'">
        {{ lastForm.statusMsg }}
    </div>

    <br>
    <form @submit="onSubmit" v-if="authenticated">
        
        <label for="title">Title:</label><br>
        <input type="text" id="title" v-model="ticket.title"/><br>

        <label for="impact">Impact:</label><br>
        <select id="impact" v-model="ticket.impact">
            <option value="Low">Low</option>
            <option value="Medium">Medium</option>
            <option value="High">High</option>
        </select><br>

        <label for="category">Category:</label><br>
        <input type="text" id="category" v-model="ticket.category"/><br>
        
        <label for="assignee">Assign to User:</label><br>
        <input type="text" id="assignee" v-model="ticket.assignee"/><br>
        
        <label for="group">Assign to Group:</label><br>
        <input type="text" id="group" v-model="ticket.group"/><br>

        <label for="description">Description:</label><br>
        <textarea cols="50" rows="6" id="description" v-model="ticket.description"/><br>
        
        <br><input type="submit" value="Create Ticket"/>
    
    </form>
</template>

<script>
import { mapGetters, mapActions } from "vuex"

export default {
    name: "TicketForm",

    data() {
        return {
            lastForm: {
                isSuccess: true,
                statusMsg: "",
            },
            ticket: {},
        };
    },

    methods: {
        ...mapActions(["createTicket"]),

        onSubmit(e) {
            e.preventDefault();
            this.saveForm();
        },
        
        async saveForm() {
            try {
                await this.createTicket(this.ticket);
                this.lastForm.isSuccess = true;
                this.lastForm.statusMsg = "Succesfully created ticket";
            }
            catch(e) {
                this.lastForm.isSuccess = false;
                this.lastForm.statusMsg = String(e);
            }
        },
    },

    computed: {
        ...mapGetters(["authenticated"]),
    },
}
</script>
