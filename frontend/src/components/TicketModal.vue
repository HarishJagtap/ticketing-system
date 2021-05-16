<template>
<div class="modal fade" :id="`ticket-${ticket.id}`" role="dialog">
    <div class="modal-dialog">
        <div class="modal-content">

            <div class="modal-header">
                <h5 class="modal-title">Ticket Details</h5>
            </div>

            <div class="modal-body">
                <p>ID: {{ ticket.id }}</p>
                <p>Title: {{ ticket.title }}</p>
                <p>Description: {{ ticket.description }}</p>
                <p>Author: {{ ticket.author }}</p>
                <p>Impact: {{ ticket.impact }}</p>
                <p v-if="ticket.category">Category: {{ ticket.category }}</p>
                <p v-if="ticket.assignee">Assigned to User: {{ ticket.assignee }}</p>
                <p v-if="ticket.group">Assigned to Group: {{ ticket.group }}</p>
            </div>

            <div class="modal-footer">
                <button data-dismiss="modal">Close</button>
            </div>

        </div>
    </div>
</div>
</template>

<script>
import { mapActions } from "vuex"

export default {
    name: "TicketModal",

    props: {
        ticketId: Number,
    },

    data() {
        return {
            ticket: Object,
        }
    },

    methods: {
        ...mapActions(["getTicket"]),
        
        async getSingleTicket() {
            try {
                this.ticket = await this.getTicket(this.ticketId);
            }
            catch(e) {}
        },
    },

    created() {
        this.getSingleTicket();
    }
};
</script>
