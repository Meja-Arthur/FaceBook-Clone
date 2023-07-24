<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
      <div class="main-left">
          <div class="p-12 bg-white border border-gray-200 rounded-lg">
              <h1 class="mb-6 text-2xl">Log in</h1>
  
              <p class="mb-6 text-grey-500">
                  Hi
                  <br>
                     Welcome Stranger
                  <br>
                  
              </p>
  
              <p class="font-bold">
                  Don't have an account?<router-link to="/signup" class="underline">Click Here</router-link>to Create one!
              </p>
          </div>
      </div>
  
      <div class="main-right">
          <div class="p-12 bg-white border border-gray-200 rounded-lg"> 
              <form class="space-y-6" v-on:submit.prevent="submitForm" ><!--Which add space between the div's -->
  
                  <div>
                      <label>E-mail</label><br>
                      <input type="email"  v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                  </div>
  
                  <div>
                      <label>Password</label><br>
                      <input type="password"  v-model="form.password" placeholder="Enter your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                  </div>

                  <template v-if="errors.length > 0">
                    <div class="bg-red-300 text-white rounded-lg p-6">
                        <p v-for="error in errors" v-bind:key="error">
                             {{ error }}
                        </p>
                    </div>      
                   </template>

  
                  <div>
                      <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">log in</button>
                  </div>
              </form>
          </div>
      </div>
  
    </div>
  </template>

  

  
<script>
import axios from 'axios';
import { useUserStore } from '../stores/user';

export default {
  setup() {
    const userStore = useUserStore();
     //using the store to manage the login
    return {
      userStore,//by returning this allows it to be used
    };
  },

  data() {
    return {
      form: {
        email: '',
        password: '',
      },
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.errors = [];

      if (this.form.email === '') {
        this.errors.push('E-mail address is missing');
      }

      if (this.form.password === '') {
        this.errors.push('Password is missing');
      }

      if (this.errors.length === 0) { // Check for errors.length instead of errors.length === ''
        try {
          const response = await axios.post('/api/login/', this.form);
          this.userStore.setTokens(response.data);
          console.log(response.data.access);
          axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access;
          const userResponse = await axios.get('/api/me/');
          this.userStore.setUserInfo(userResponse.data);
          this.$router.push('/feed');
        } catch (error) {
          console.log('Error:', error);
        }
      }
    },
  },
};
</script>

<style>

</style>


 