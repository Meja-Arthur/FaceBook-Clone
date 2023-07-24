<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
        <div class="p-12 bg-white border border-gray-200 rounded-lg">
            <h1 class="mb-6 text-2xl">Sign up</h1>

            <p class="mb-6 text-grey-500">
                Hi
                <br>
                by accepting this notice you agree to the conditions as outlined 
                If you do not agree with the conditions as outlined
                <br>
                DO NOT SIGN UP
            </p>

            <p class="font-bold">
                Already have an account?<router-link to="/login" class="underline">Click Here</router-link> to log in!
            </p>
        </div>
    </div>

    <div class="main-right">
        <div class="p-12 bg-white border border-gray-200 rounded-lg"> 
            <form  class="space-y-6"  v-on:submit.prevent="submitForm"><!--Which add space between the div's -->
                <div>
                    <label>Name</label><br>
                    <input type="text" v-model="form.name"  placeholder="Name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                </div>

                <div>
                    <label>E-mail</label><br>
                    <input type="email"  v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                </div>

                <div>
                    <label>Password</label><br>
                    <input type="password"  v-model="form.password1" placeholder="Enter your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                </div>

                <div>
                    <label>Password</label><br>
                    <input type="password"  v-model="form.password2" placeholder="Comfirm your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                </div>

                <template v-if="errors.length > 0">
                    <div class="bg-red-300 text-white rounded-lg p-6">
                        <p v-for="error in errors" v-bind:key="error">
                             {{ error }}
                        </p>
                    </div>      
                </template>

                <div>
                    <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</button>
                </div>
            </form>
        </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()
        return {
            toastStore
        }
    },

    data() {
        return{
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: []
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            // validation of any error that might occure in login process
            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name address is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The passwords does not match')
            }

            if (this.errors.length === 0) {
                axios

                    .post('/api/signup/', this.form)
                    
                    .then(response => {
                        if (response.data.message === 'success') {

                            this.toastStore.showToast(5000, 'User created successfully. Please log in', 'bg-emerald-500')
                   
                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''      

                        } else {
                            this.toastStore.showToast(5000, 'something ent wrong. Please try again', 'bg-red-300')
                        }
                        this.$router.push('/login')
                    })

                    .catch(error => {
                        console.log('error', error)
                    })
            }

        }
    }


}
</script>

<style>

</style>