import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductView from "@/views/ProductView.vue";
import SignupView from "@/views/SignupView.vue";
import LoginView from "@/views/LoginView.vue";
import LogoutView from "@/views/LogoutView.vue";
import ProductCreateView from "@/views/ProductCreateView.vue";
import ProfileUserView from "@/views/ProfileUserView.vue";
import EditProfileView from "@/views/EditProfileView.vue";
import ProfileView from "@/views/ProfileView.vue";
import EditPassword from "@/views/EditPassword.vue";
import ExFilterBar from "@/components/ExFilterBar.vue";


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/game/:gameId',
      name: 'game',
      component: ProductView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/profile/:userId',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/edit-profile/:userId',
      name: 'edit_profile',
      component: EditProfileView
    },
    {
      path: '/test/:gameId',
      name: 'test',
      component: ExFilterBar
    },
    {
      path: '/edit-password/:userId',
      name: 'edit_password',
      component: EditPassword
    },
    {
      path: '/user_profile/:userId',
      name: 'user_profile',
      component: ProfileUserView
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogoutView
    },
    {
      path: '/create_product',
      name: 'create_product',
      component: ProductCreateView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router