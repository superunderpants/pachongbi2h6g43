	import Vue from 'vue';
//配置路由
	import VueRouter from 'vue-router'
	Vue.use(VueRouter);
//1.创建组件
	import Index from '@/views/index'
	import Home from '@/views/home'
	import Board from '@/views/board'
	import Login from '@/views/login'
	import NotFound from '@/views/404'
	import UpdatePassword from '@/views/update-password'
	import pay from '@/views/pay'
	import register from '@/views/register'
	import center from '@/views/center'
	import yonghu from '@/views/modules/yonghu/list'
	import autohome from '@/views/modules/autohome/list'
	import zixunfenlei from '@/views/modules/zixunfenlei/list'
	import xingyezixun from '@/views/modules/xingyezixun/list'
	import zixunjiedu from '@/views/modules/zixunjiedu/list'
	import news from '@/views/modules/news/list'
	import chat from '@/views/modules/chat/list'
	import users from '@/views/modules/users/list'
	import discussautohome from '@/views/modules/discussautohome/list'
	import discussxingyezixun from '@/views/modules/discussxingyezixun/list'
import qichexinxi from '@/views/modules/qichexinxi/list'
import config from '@/views/modules/config/list'

//2.配置路由   注意：名字
export const routes = [{
	path: '/',
	name: '系统首页',
	component: Index,
	children: [{
		// 这里不设置值，是把main作为默认页面
		path: '/',
		name: '系统首页',
		component: Home,
		meta: {icon:'', title:'center', affix: true}
	}, {
		path: '/updatePassword',
		name: '修改密码',
		component: UpdatePassword,
		meta: {icon:'', title:'updatePassword'}
	}, {
		path: '/pay',
		name: '支付',
		component: pay,
		meta: {icon:'', title:'pay'}
	}, {
		path: '/center',
		name: '个人信息',
		component: center,
		meta: {icon:'', title:'center'}
	}
	,{
		path: '/yonghu',
		name: '用户',
		component: yonghu
	}
	,{
		path: '/autohome',
		name: '新能源资讯',
		component: autohome
	}
	,{
		path: '/autohomestat',
		name: '新能源资讯统计',
		component: autohome
	}
	,{
		path: '/zixunfenlei',
		name: '资讯分类',
		component: zixunfenlei
	}
	,{
		path: '/xingyezixun',
		name: '行业资讯',
		component: xingyezixun
	}
	,{
		path: '/xingyezixunstat',
		name: '行业资讯统计',
		component: xingyezixun
	}
	,{
		path: '/zixunjiedu',
		name: '资讯解读',
		component: zixunjiedu
	}
	,{
		path: '/news',
		name: '系统公告',
		component: news
	}
	,{
		path: '/chat',
		name: 'ai问答',
		component: chat
	}
	,{
		path: '/users',
		name: '管理员',
		component: users
	}
	,{
		path: '/discussautohome',
		name: '新能源资讯',
		component: discussautohome
	}
	,{
		path: '/discussxingyezixun',
		name: '行业资讯评论',
		component: discussxingyezixun
		}
		,{
			path: '/qichexinxi',
			name: '汽车信息',
			component: qichexinxi
		}
		,{
			path: '/config/:type',
			name: '配置管理',
			component: config
	}
	]
	},
	{
		path: '/login',
		name: 'login',
		component: Login,
		meta: {icon:'', title:'login'}
	},
	{
		path: '/board',
		name: 'board',
		component: Board,
		meta: {icon:'', title:'board'}
	},
	{
		path: '/register',
		name: 'register',
		component: register,
		meta: {icon:'', title:'register'}
	},
	{
		path: '*',
		component: NotFound
	}
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
	mode: 'hash',
	/*hash模式改为history*/
	routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}
export default router;
