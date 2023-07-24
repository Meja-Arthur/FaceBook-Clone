<template>
    <div class="mx-w-7xl mx-auto grid grid-cols-4 gap-4">

        <div class="main-left col-span-1">
            <div class="p-4 bg-white  border border-gray-200 text-center rounded-lg">
                <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full">
                <p><strong>{{ user.name }}</strong></p>
                <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
                    <p class="text-xs text-gray-500">120 posts</p>
                </div>

            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg "
                v-if="friendlyRequests.length"
            >

                <h2 class=" mb-6 text-xl">Friendship request</h2>

                <div
                    class="p-4 text-center bg-gray-100 rounded-lg"
                    v-for=" friendlyRequest in friendlyRequests"
                    v-bind:key="friendlyRequest.id"
                 >
                    <img src="https://i.pravatar.cc/100?img=70" class="mb-6 mx-auto rounded-full">

                    <p>
                        <strong>
                            <RouterLink :to="{name: 'profile', params:{'id': friendlyRequest.created_by.id}}">
                                {{friendlyRequest.created_by.name }}
                            </RouterLink>
                        </strong>
                    </p>

                    <div class="mt-6 flex space-x-a justify-around">
                        <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
                        <p class="text-xs text-gray-500">128 post</p>
                    </div>

                    <div class="mt-6 space-x-4">

                        <button class="inline-block 
                        py-4 px-6 bg-green-600 text-white rounded-lg"
                         @click="handleRequest('accepted', friendlyRequest.created_by.id)">Accept</button>


                        <button class="inline-block py-4 px-6 bg-red-600 text-white rounded-lg" 
                        @click="handleRequest('rejected', friendlyRequest.created_by.id)">Reject</button>
                    </div>


                </div>
                <hr>

            </div>

            

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-2 gap-4"
                v-if="friends.length"
            >

                <div
                    class="p-4 text-center bg-gray-100 rounded-lg"
                    v-for="user in friends"
                    v-bind:key="user.id"
                 >
                    <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full">

                    <p>
                        <strong>
                            <RouterLink :to="{name: 'profile', params:{'id': user.id}}">{{ user.name }}</RouterLink>
                        </strong>
                    </p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
                        <p class="text-xs text-gray-500">128 post</p>
                    </div>
                </div>

            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleKnown/>
            <Trends/>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import PeopleKnown from '../components/PeopleKnown.vue';
import Trends from '../components/Trends.vue'

import { useUserStore } from '@/stores/user';

export default {

    setup() {
    const userStore = useUserStore();
        return {
        userStore,
    };

  },

    components: {
        PeopleKnown,
        Trends,
    },
  
    data() {
        return {
            user: {},// here we are importing the owner of the profile 
            friendlyRequests: {},
            friends: {},
        }
    },

    mounted() {
        this.getFriends()
    },

    methods: {
        getFriends() {
            axios
            // using the user's id to filter all the request sent to him
               .get(`/api/friends/${this.$route.params.id}/`)

               .then(response => {
                console.log('data', response.data)

                this.friendlyRequests = response.data.requests
                this.friends = response.data.friends
                this.user = response.data.user
            
               })
               .catch(error => {
                console.log('error', error)
               })
        },

        
        //handling the response of the request either accepted or rejected 
        // ${pk} is the primary key of the user to whom the request is from  and then we pass in the status of the request 
        handleRequest(status, pk) {
            console.log('handleRequest', status)
            axios
              .post(`/api/friends/${pk}/${status}/`)
              .then(response => {
                console.log('data', response.data)
              })
              .catch(error => {
                console.log('error', error)
              })
        }
    }

}
</script>

<style>

</style>