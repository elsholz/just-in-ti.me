import moment from 'moment'

const routes = [
  // {
  //   path: '/:year/:week',
  //   children: [
  //     { path: '', component: () => import('pages/IndexPage.vue') }
  //   ]
  // },
  // {
  //   path: '/:year',

  // },
  {
    path: '/impressum',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: import('pages/ImpressumPage.vue') }
    ]
  },
  {
    path: '/privacy',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: import('pages/PrivacyPage.vue') }
    ]
  },
  {
    path: '',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        redirect: to => {
          const d = new Date()
          return { path: '/' + d.getFullYear() }
        },
      },
      {
        path: ':year',
        children: [
          {
            path: '',
            redirect: to => {
              const d = new Date()
              let week

              if (d.getFullYear().toString() === to.params.year) {
                week = moment().isoWeek()
              }
              else {
                week = 1
              }

              return { path: '/' + to.params.year + '/' + week }
            },
          },
          {
            path: ':week',
            children: [
              { path: '', component: () => import('pages/IndexPage.vue') }
            ]
          },
        ]
      },
    ]
  },


  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
