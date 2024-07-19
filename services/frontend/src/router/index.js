import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue';
import Docs from '@/views/Docs.vue';
import Create from '@/views/Create.vue';
import Read from '@/views/Read.vue';
import Update from '@/views/Update.vue';
import Delete from '@/views/Delete.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),

  routes: [
    {
      path: '/',
      name: 'Home',
      component:HomeView
    },
    {
      path: '/docs',
      name: 'Docs',
      component:Docs
    },
    {
      path: '/create',
      name: 'Create',
      component:Create
    },
    {
      path: '/read',
      name: 'Read',
      component:Read
    },
    {
      path: '/update',
      name: 'Update',
      component:Update
    },
    {
      path: '/Delete',
      name: 'Delete',
      component:Delete
    }

  ]
})

export default router
