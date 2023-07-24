import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import FeedView from '../views/FeedView.vue'
import MessagesView from '../views/MessagesView.vue'
import SearchView from '../views/SearchView.vue'
import ProfileView from '../views/ProfileView.vue'
import FriendsView from '../views/FriendsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/login',
      name: 'login',
      component:  LoginView
    },
    {
      path: '/feed',
      name: 'feed',
      component:  FeedView
    },
    {
      path: '/message',
      name: 'message',
      component:  MessagesView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView
    },

    {
      path: '/profile/:id/friends',
      name: 'friends',
      component: FriendsView
    },

  ]
})

export default router
