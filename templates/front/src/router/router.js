import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import autohomeList from '../pages/autohome/list'
import autohomeDetail from '../pages/autohome/detail'
import autohomeAdd from '../pages/autohome/add'
import zixunfenleiList from '../pages/zixunfenlei/list'
import zixunfenleiDetail from '../pages/zixunfenlei/detail'
import zixunfenleiAdd from '../pages/zixunfenlei/add'
import xingyezixunList from '../pages/xingyezixun/list'
import xingyezixunDetail from '../pages/xingyezixun/detail'
import xingyezixunAdd from '../pages/xingyezixun/add'
import zixunjieduList from '../pages/zixunjiedu/list'
import zixunjieduDetail from '../pages/zixunjiedu/detail'
import zixunjieduAdd from '../pages/zixunjiedu/add'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import discussautohomeList from '../pages/discussautohome/list'
import discussautohomeDetail from '../pages/discussautohome/detail'
import discussautohomeAdd from '../pages/discussautohome/add'
import discussxingyezixunList from '../pages/discussxingyezixun/list'
import discussxingyezixunDetail from '../pages/discussxingyezixun/detail'
import discussxingyezixunAdd from '../pages/discussxingyezixun/add'
import qichexinxiList from '../pages/qichexinxi/list'
import qichexinxiDetail from '../pages/qichexinxi/detail'
import qichexinxiAdd from '../pages/qichexinxi/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'autohome',
					component: autohomeList
				},
				{
					path: 'autohomeDetail',
					component: autohomeDetail
				},
				{
					path: 'autohomeAdd',
					component: autohomeAdd
				},
				{
					path: 'zixunfenlei',
					component: zixunfenleiList
				},
				{
					path: 'zixunfenleiDetail',
					component: zixunfenleiDetail
				},
				{
					path: 'zixunfenleiAdd',
					component: zixunfenleiAdd
				},
				{
					path: 'xingyezixun',
					component: xingyezixunList
				},
				{
					path: 'xingyezixunDetail',
					component: xingyezixunDetail
				},
				{
					path: 'xingyezixunAdd',
					component: xingyezixunAdd
				},
				{
					path: 'zixunjiedu',
					component: zixunjieduList
				},
				{
					path: 'zixunjieduDetail',
					component: zixunjieduDetail
				},
				{
					path: 'zixunjieduAdd',
					component: zixunjieduAdd
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'discussautohome',
					component: discussautohomeList
				},
				{
					path: 'discussautohomeDetail',
					component: discussautohomeDetail
				},
				{
					path: 'discussautohomeAdd',
					component: discussautohomeAdd
				},
				{
					path: 'discussxingyezixun',
					component: discussxingyezixunList
				},
				{
					path: 'discussxingyezixunDetail',
					component: discussxingyezixunDetail
				},
				{
					path: 'discussxingyezixunAdd',
					component: discussxingyezixunAdd
				},
				{
					path: 'qichexinxi',
					component: qichexinxiList
				},
				{
					path: 'qichexinxiDetail',
					component: qichexinxiDetail
				},
				{
					path: 'qichexinxiAdd',
					component: qichexinxiAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
