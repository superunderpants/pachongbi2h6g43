<template>
	<div class="main-containers">
		<div class="body-containers">
			<div class="top-container">
				<!-- info -->
				<div class="top_title">
					<span @click="goMenu('/index/home')">基于Python的网络爬虫与数据可视化分析平台</span>
				</div>
				<div class="top_tel"></div>
			

				<el-dropdown class="dropdown-box" @command="handleCommand" trigger="click">
					<div class="el-dropdown-link" v-show="Token">
						<img class="top_avatar2" v-show="headportrait&&Token" :src="headportrait?baseUrl + headportrait:require('@/assets/avator.png')">
						<span class="top_label2">欢迎</span>
						<span class="top_nickname2">{{username}}</span>
						<span class="icon iconfont icon-xiala"></span>
					</div>
					<div class="el-dropdown-link" v-show="!Token">
						<div class="login-item" @click="toLogin">
							<span class="icon iconfont icon-touxiang03"></span>
							登录
						</div>
					</div>
					<el-dropdown-menu class="top-el-dropdown-menu" slot="dropdown" v-show="Token">
						<el-dropdown-item v-show="notAdmin" class="user-item" :command="'user'">
							<span class="icon iconfont icon-touxiang09"></span>
							个人中心
						</el-dropdown-item>
						<el-dropdown-item class="board-item" :command="'board'" v-show="Token&&boardAuth()">
							<span class="icon iconfont icon-xiaoliang8"></span>
							看板						</el-dropdown-item>
						<el-dropdown-item class="register-item" :command="'register'">
							<span class="icon iconfont icon-shanchu16"></span>
							退出
						</el-dropdown-item>
					</el-dropdown-menu>
				</el-dropdown>
			</div>


			<div class="menu-preview">
				<div class="menu-list">
					<div class="menu-home" :class="activeMenu=='/index/home'?'menu-active':''" @click="goMenu('/index/home')">
						<div class="title">
							<span class="icon iconfont icon-shouye-zhihui"></span>
							<div class="text">首页</div>
						</div>
					</div>
					<div  class="menu-item" v-for="(item,index) in menuList" :key="index" @mouseenter="menuShowClick4(index)" @mouseleave="menuShowClick4(-1)" :class="activeMenu==item.url?'menu-active':''" @click.stop="goMenu(item.url)">
						<div class="title">
							<span :class="iconArr[index]"></span>
							<div class="text">{{item.name}}</div>
						</div>
						<transition name="el-zoom-in-top">
							<div v-if="showType4==index&&item.hasCate" class="menu-child-list">
								<div class="child-item" v-for="(items,indexs) in item.cateList" :key="indexs" @click.stop="cateClick(item.url,items)">{{items}}</div>
							</div>
						</transition>
					</div>
					<div class="menu-item" @click="goChat" v-if="Token">
						<div class="title">
							<span class="icon iconfont icon-shouye-zhihui"></span>
							<div class="text">
								ai问答
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="banner-preview" v-if="carouselChange()">
				<div class="swiper-container mySwiper3">
					<div class="swiper-wrapper">
						<div class="swiper-slide" v-for="item in carouselList" :key="item.id">
							<div class="swiper-item">
								<el-image v-if="preHttp(item.value)" @click="carouselClick(item.url)" :src="item.value" fit="cover"></el-image>
								<el-image v-else @click="carouselClick(item.url)" :src="baseUrl + item.value" fit="cover"></el-image>
							</div>
						</div>
					</div>
					<div class="banner-hidden">
					</div>
					<!-- Add Pagination -->
					<div class="swiper-pagination"></div>
					<!-- Add Arrows -->
					<div class="swiper-button-next">
						<span class="icon iconfont icon-jiantou18"></span>
					</div>
					<div class="swiper-button-prev">
						<span class="icon iconfont icon-jiantou39"></span>
					</div>
				</div>
			</div>
			<router-view id="scrollView"></router-view>
			
			<div class="bottom-preview">
				<div class="footer"><div v-html="bottomContent"></div></div>
			</div>
		</div>
		
		<el-dialog title="ai问答" :visible.sync="chatFormVisible" width="60%" :before-close="chatClose">
			<div class="chat-content" id="chat-content">
				<div :key="item.id" v-for="item in chatList">
					<div v-if="item.addtime" style="width: 100%;text-align: center;font-size: 10px;color: #666;">{{timeFormat(item.addtime)}}</div>
					<div v-if="item.ask" class="right-content">
						<div style="display: flex;align-items: flex-start;">
							<el-alert v-if="item.type==1" class="text-content" :title="item.ask" :closable="false"
								type="warning" style="white-space:pre-line;"></el-alert>
							<el-image v-else-if="item.type==2" :src="baseUrl + item.ask" style="width: 150px;height: 150px;" fit="cover" :preview-src-list="[baseUrl + item.ask]"></el-image>
							<video v-else-if="item.type==3" :src="baseUrl + item.ask" style="width: 280px;" controls></video>
							<el-button v-else-if="item.type==4" type="primary" size="mini" @click="download(item.ask)">文件预览</el-button>
							<img :src="item.uimage?(baseUrl + item.uimage.split(',')[0]):require('@/assets/service.png')" style="width: 30px;height: 30px;border-radius: 50%;margin: 0 0 0 5px;" alt="">
						</div>
					</div>
					<div v-else class="left-content">
						<div style="display: flex;align-items: flex-start;">
							<img :src="item.uimage?(baseUrl + item.uimage.split(',')[0]):require('@/assets/AI.png')" style="width: 30px;height: 30px;border-radius: 50%;margin: 0 5px 0 0;" alt="">
							<el-alert v-if="item.type==1" class="text-content" :title="item.reply" :closable="false"
								type="success" style="white-space:pre-line;"></el-alert>
							<el-image v-else-if="item.type==2" :src="baseUrl + item.reply" style="width: 150px;height: 150px;" fit="cover" :preview-src-list="[baseUrl + item.reply]"></el-image>
							<video v-else-if="item.type==3" :src="baseUrl + item.reply" style="width: 280px;" controls></video>
							<el-button v-else-if="item.type==4" type="primary" size="mini" @click="download(item.reply)">文件预览</el-button>
						</div>
					</div>
					<div class="clear-float"></div>
				</div>
			</div>
			<div v-if="aiLoading" v-loading="true" element-loading-background="rgba(255, 255, 255, 0.2)" style="text-align: center">
				AI正在解答您的问题，请稍后...
			</div>
			<div slot="footer" class="dialog-footer">
				<div v-if="askShow"
					style="padding-bottom: 10px;display: flex;align-items: center;justify-content: center;">
					<el-upload class="upload-demo" :action="uploadUrl" :on-success="uploadSuccess" accept="image/*"
						:show-file-list="false">
						<el-button size="mini" type="success">上传图片</el-button>
					</el-upload>
					<el-upload class="upload-demo" :action="uploadUrl" :on-success="uploadSuccess2" accept="video/*"
						:show-file-list="false">
						<el-button size="mini" type="success" style="margin: 0 0 0 10px;">上传视频</el-button>
					</el-upload>
					<el-upload class="upload-demo" :action="uploadUrl" :on-success="uploadSuccess3"
						:show-file-list="false">
						<el-button size="mini" type="success" style="margin: 0 0 0 10px;">上传文件</el-button>
					</el-upload>
					<el-button size="mini" type="primary" style="margin: 0 0 0 10px;" @click="askChange">
						转{{askType==1?'人工服务':'智能回复'}}</el-button>
				</div>
				<div style="width: 100%;display: flex;align-items: center;justify-content: space-between;">
					<img style="width: 30px;cursor: pointer;" @click="askShow = !askShow" src="../assets/jiahao.png">
					<el-input @keydown.enter.native="addChat(null)" v-model="form.ask" placeholder="请输入内容" style="width: calc(100% - 110px);">
					</el-input>
					<el-button type="primary" @click="addChat(null)">发送</el-button>
					<div style="position: relative;" v-if="askType==2">
						<span @click="showEmoji=!showEmoji" class="icon iconfont icon-gerenzhongxin-zhihui" style="font-size: 30px;color: #666;cursor: pointer;"></span>
						<picker
							:include="['people', 'Smileys']"
							:showSearch="false"
							:showPreview="false"
							:showCategories="false"
							@select="addEmoji"
							v-if="showEmoji"
							:backgroundImageFn="((set,sheetSize)=>{
								return require('@/assets/32.png')
							})"
							style="position: absolute;bottom: 40px;left: -100px;"
						/>
					</div>
				</div>
			</div>
		</el-dialog>
		<div class="audioAnimation-box" v-if="audio.length" :style="audioPlayerWrapStyle" @mouseover="showmouseover">
			<div @click="suoClick"
				style="position: absolute;top: -20px;right: 40%;background: #fff;border-radius: 50% 50% 0 0;font-size: 0;width: 30px;height: 30px;display: flex;justify-content: center;align-items: center;cursor: pointer;">
				<img v-if="suoType" style="width: 20px;height: 20px;" src="../assets/suo.png">
				<img v-else style="width: 20px;height: 20px;" src="../assets/jiesuo.png">
			</div>
			<div class="audio-external-volume" @mousedown.stop @click.stop>
				<button type="button" class="audio-external-volume__trigger" aria-label="调节音量">
					<span class="audio-external-volume__icon" aria-hidden="true">
						<svg viewBox="0 0 24 24" width="16" height="16" fill="none" xmlns="http://www.w3.org/2000/svg">
							<path d="M11 5L6 9H2v6h4l5 4V5z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>
							<template v-if="playerVolumePct > 0">
								<path d="M15.54 8.46a5 5 0 010 7.07" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
								<path v-if="playerVolumePct > 55" d="M19.07 4.93a9 9 0 010 14.14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
							</template>
							<path v-else d="M14 9l6 6M14 15l6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
						</svg>
					</span>
				</button>
				<div class="audio-external-volume__panel">
					<div class="audio-external-volume__slider">
						<input
							type="range"
							class="audio-external-volume__range"
							min="0"
							max="100"
							step="1"
							:value="playerVolumePct"
							:style="{ '--vol': playerVolumePct + '%' }"
							@input="onExternalVolumeInput"
						/>
					</div>
					<span class="audio-external-volume__pct">{{ playerVolumePct }}%</span>
				</div>
			</div>
			<aplayer :float="false" repeat="repeat-all" ref="aplayer" id="aplayer" :music="audio[audioIndex]" @timeupdate="timeChange" @play="playing"
				@volumechange="syncPlayerVolumeFromAudio"
				:list="audio" :showLrc="audio[audioIndex].lrc&&audio[audioIndex].lrc!=''?true:false" :listFolded="true" :autoplay="true" listMaxHeight="180px" :lrcType="1"></aplayer>
		</div>
	</div>
</template>

<script>
	import Vue from 'vue'
	import Swiper from "swiper";
	import axios from 'axios'
	import { Picker } from "emoji-mart-vue";
	import timeMethod from '@/common/timeMethod'
	import {
		WebsocketMixin
	} from '@/mixins/WebsocketMixin'
export default {
	components:{
		Picker
	},
	mixins: [WebsocketMixin],
	data() {
		return {
			activeIndex: '0',
			baseUrl: '',
			carouselList: [],
			carouselForm: {
				inHome: true,
				inOther: true,
			},
			mySwiper3Timer: null,
			menuList: [],
			askType: 1, //1为智能回复 2为人工服务
			chatFormVisible: false,
			chatList: [],
			headers: {
				Token: localStorage.getItem('frontToken')
			},
			uploadUrl: this.$config.baseUrl + 'file/upload',
			askShow: false,
			aiLoading: false,
			showEmoji: false,
			form: {
				ask: '',
			},
			headportrait: localStorage.getItem('frontHeadportrait')?localStorage.getItem('frontHeadportrait'):'',
			Token: localStorage.getItem('frontToken'),
			username: localStorage.getItem('username'),
			notAdmin: localStorage.getItem('frontSessionTable')!='"users"',
			iconArr: [
				'el-icon-star-off',
				'el-icon-goods',
				'el-icon-warning',
				'el-icon-question',
				'el-icon-info',
				'el-icon-help',
				'el-icon-picture-outline-round',
				'el-icon-camera-solid',
				'el-icon-video-camera-solid',
				'el-icon-video-camera',
				'el-icon-bell',
				'el-icon-s-cooperation',
				'el-icon-s-order',
				'el-icon-s-platform',
				'el-icon-s-operation',
				'el-icon-s-promotion',
				'el-icon-s-release',
				'el-icon-s-ticket',
				'el-icon-s-management',
				'el-icon-s-open',
				'el-icon-s-shop',
				'el-icon-s-marketing',
				'el-icon-s-flag',
				'el-icon-s-comment',
				'el-icon-s-finance',
				'el-icon-s-claim',
				'el-icon-s-opportunity',
				'el-icon-s-data',
				'el-icon-s-check'
			],
			bottomContent: '',
			musicType: false,
			showTimer: null,
			showType: false,
			suoType:false,
			playerVolumePct: 80,
			showType4: -1,
			indexBgUrl: '',
		}
	},
	async created() {
		this.$http.get('config/info?name=fTopLogo',).then(rs=>{this.indexLogoUrl = rs.data.data?rs.data.data.value:''})
		this.baseUrl = this.$config.baseUrl;
		this.menuList = this.$config.indexNav;
		this.getCarousel();
		if(localStorage.getItem('frontToken') && localStorage.getItem('frontToken')!=null) {
			this.getSession()
		}
		this.cateList = this.$config.cateList
		if(this.cateList.length){
			for(let x in this.menuList){
				for(let i in this.cateList){
					if(this.menuList[x].name==this.cateList[i].name){
						await this.$http.get(`option/${this.cateList[i].refTable}/${this.cateList[i].refColumn}`).then(rs=>{
							this.menuList[x].cateList = rs.data.data
							this.menuList[x].hasCate = true
						})
					}
				}
			}
		}
	},
	mounted() {
		this.activeIndex = localStorage.getItem('keyPath') || '0';
		this.musicType = localStorage.getItem('musicType') ? true : false;


		// banner
		setTimeout(()=>{
			this.mySwiper3Timer = new Swiper(".mySwiper3", {"navigation":{"nextEl":".swiper-button-next","prevEl":".swiper-button-prev"},"pagination":{"el":".swiper-pagination","clickable":true},"slidesPerView":3,"speed":300,"autoplay":{"delay":2500,"disableOnInteraction":false},"effect":"fade"})
		}, 500)

	},
	computed: {
		activeMenu() {
			const route = this.$route
			const {
				meta,
				path
			} = route
			// if st path, the sidebar will highlight the path you sete
			if (meta.activeMenu) {
				return meta.activeMenu
			}
			return path
		},
		audioIndex: {
			get() {
				return this.$store.state.app.audioIndex
			},
			set(val) {
				return this.$store.state.app.audioIndex = val
			}
		},
		audio: {
			get() {
				return this.$store.state.app.audio
			},
			set(val) {
				return this.$store.state.app.audio = val
			}
		},
		audioPlayerWrapStyle() {
			const cur = this.audio[this.audioIndex] || {}
			const hasLrc = cur.lrc && cur.lrc !== ''
			const hideOffset = hasLrc ? 98 : 68
			return {
				width: '100%',
				position: 'fixed',
				left: 0,
				zIndex: 99999,
				bottom: this.showType ? '0px' : `-${hideOffset}px`,
				transition: 'bottom 0.3s ease',
				pointerEvents: 'auto',
			}
		},
	},
	watch: {
		$route(newValue) {
			let that = this
			let url = window.location.href
			let arr = url.split('#')
			for (let x in this.menuList) {
				if (newValue.path == this.menuList[x].url) {
					this.activeIndex = x
				}
			}
			this.Token = localStorage.getItem('frontToken')
			if(arr[1]!='/index/home'){
				var element = document.getElementById('scrollView');
				var distance = element.offsetTop;
				window.scrollTo( 0, distance )
			}else{
				setTimeout(()=>{
					window.scrollTo( 0, 0 )
				},100)
			}
		},
		headportrait(){
			this.$forceUpdate()
		},
		audio(newValue) {
			this.audioIndex = this.$store.state.app.audioIndex
			if (newValue && newValue.length) {
				this.$nextTick(() => this.syncPlayerVolumeFromAudio())
			}
		},
		audioIndex() {
			this.showmouseover()
			this.$nextTick(() => {
				if (this.$refs.aplayer) {
					this.$refs.aplayer.play()
					this.syncPlayerVolumeFromAudio()
				}
			})
			this.$forceUpdate()
		},
	},
	methods: {
		cateClick(url,fenlei){
			this.$router.push(url + '?homeFenlei=' + fenlei);
		},
		preHttp(str) {
			return str && str.substr(0,4)=='http';
		},

		async getSession() {
			await this.$http.get(`${localStorage.getItem('UserTableName')}/session`, {emulateJSON: true}).then(async res => {
				if (res.data.code == 0) {
					localStorage.setItem('sessionForm',JSON.stringify(res.data.data))
					localStorage.setItem('frontUserid', res.data.data.id);
					if(res.data.data.vip) {
						localStorage.setItem('vip', res.data.data.vip);
					}
					if(res.data.data.touxiang) {
						this.headportrait = res.data.data.touxiang
						localStorage.setItem('frontHeadportrait', res.data.data.touxiang);
					} else if(res.data.data.headportrait) {
						this.headportrait = res.data.data.headportrait
						localStorage.setItem('frontHeadportrait', res.data.data.headportrait);
					}
				}
			});
		},
		handleSelect(keyPath) {
			if (keyPath) {
				localStorage.setItem('keyPath', keyPath)
			}
		},
		toLogin() {
		  this.$router.push('/login');
		},
		async logout() {
			await this.$http.post(`${localStorage.getItem('frontSessionTable')}/logout`).then(rs=>{
				localStorage.clear();
				Vue.http.headers.common['Token'] = "";
				this.$router.push('/index/home');
				this.activeIndex = '0'
				localStorage.setItem('keyPath', this.activeIndex)
				this.Token = ''
				this.$forceUpdate()
				this.$message({
					message: '登出成功',
					type: 'success',
					duration: 1000,
				});
			})
		},
		getCarousel() {
			this.$http.get('config/list', {params: {type: 1,limit: 100,type: 1}}).then(res => {
				if (res.data.code == 0) {
					this.carouselList = res.data.data.list;
				}
			});
		},
		// 轮播图跳转
		carouselClick(url) {
			if (url) {
				if (url.indexOf('https') != -1) {
					window.open(url)
				} else {
					this.$router.push(url)
				}
			}
		},
		carouselChange(){
			let url = window.location.href
			let arr = url.split('#')
			return (this.carouselForm.inHome&&arr[1]=='/index/home')||(this.carouselForm.inOther&&arr[1]!='/index/home')
		},
		goBoard(){
			localStorage.setItem('Token', localStorage.getItem('frontToken'));
			localStorage.setItem('role', localStorage.getItem('frontRole'));
			localStorage.setItem('sessionTable', localStorage.getItem('frontSessionTable'));
			localStorage.setItem('headportrait', localStorage.getItem('frontHeadportrait'));
			localStorage.setItem('userid', Number(localStorage.getItem('frontUserid')));
			localStorage.setItem('adminName', localStorage.getItem('username'));
			localStorage.setItem('userForm', JSON.stringify(localStorage.getItem('sessionForm')));
			window.location.href = `${this.$config.baseUrl}admin/dist/index.html#/board?frontType=1`
			
		},
		boardAuth(){
			if(this.isAuth('hasBoard','查看')||this.isBackAuth('hasBoard','查看')) {
				return true
			}
			return false
		},
		chatTimeChange() {
			let chatList = JSON.parse(JSON.stringify(this.chatList)).reverse()
			if(!chatList.length) {
				return true
			}
			if(chatList[0].reply&&chatList[0].reply=="您好，有什么可以帮您？") {
				return false
			}
			let lastTime = new Date().getTime();
			const currentTime = new Date(chatList[0].addtime).getTime();
			const timeDiff = (currentTime - lastTime) / 1000 / 60; // 转换为分钟
			if (timeDiff < 3) {
				return false
			}
			return true
		},
		formatMessages(messages) {
			let lastTime = null;
			messages.forEach((message, index) => {
				const currentTime = new Date(message.addtime).getTime();
				if (lastTime !== null) {
					const timeDiff = (currentTime - lastTime) / 1000 / 60; // 转换为分钟
					if (timeDiff < 3) {
						message.addtime = ''; // 如果小于3分钟，不显示时间
					}
				}
				lastTime = currentTime;
			});
			return messages;
		},
		timeFormat(time) {
			const Time = timeMethod.getTime(time).split("T");
			//当前消息日期属于周
			const week = timeMethod.getDateToWeek(time);
			//当前日期0时
			const nti = timeMethod.setTimeZero(timeMethod.getNowTime());
			//消息日期当天0时
			const mnti = timeMethod.setTimeZero(timeMethod.getTime(time));
			//计算日期差值
			const diffDate = timeMethod.calculateTime(nti, mnti);
			//本周一日期0时 （后面+1是去除当天时间）
			const fwnti = timeMethod.setTimeZero(timeMethod.countDateStr(-timeMethod.getDateToWeek(timeMethod
				.getNowTime()).weekID + 1));
			//计算周日期差值
			const diffWeek = timeMethod.calculateTime(mnti, fwnti);
		
			if (diffDate === 0) { //消息发送日期减去当天日期如果等于0则是当天时间
				return Time[1].slice(0, 5);
			} else if (diffDate < 172800000) { //当前日期减去消息发送日期小于2天（172800000ms）则是昨天-  一天最大差值前天凌晨00:00:00到今天晚上23:59:59
				return "昨天 " + Time[1].slice(0, 5);
			} else if (diffWeek >= 0) { //消息日期减去本周一日期大于0则是本周
				return week.weekName;
			} else { //其他时间则是日期
				return Time[0].slice(5, 10);
			}
		},
		addEmoji(e) {
			this.form.ask += e.native;
			this.showEmoji = false
		},
		async getChatList() {
			await this.$http.get('chat/list', {params: { userid: Number(localStorage.getItem('frontUserid')), sort: 'addtime', order: 'asc',limit: 1000 }}).then(res => {
				if (res.data.code == 0) {
					this.chatList = this.formatMessages(res.data.data.list);
					let div = document.getElementsByClassName('chat-content')[0]
					setTimeout(() => {
						if (div){
							div.scrollTop = div.scrollHeight
						}
					}, 0)
				}
			});
		},
		addChat(ask=null,type=1) {
			let params = JSON.parse(JSON.stringify(this.form))
			if(params.ask==''&&ask==null){
				this.$message.error('内容不能为空')
				return false
			}
			if(ask){
				params.ask = ask
			}
			params.type = type
			params.uimage = localStorage.getItem('frontHeadportrait')
			params.uname = localStorage.getItem('username')
			params.userid = Number(localStorage.getItem('frontUserid'))
			this.$http.post('chat/add', params).then(res => {
				if (res.data.code == 0) {
					this.getChatList();
					if (this.askType == 1 && ask == null) {
						let ask2 = JSON.parse(JSON.stringify(this.form.ask))
						this.getChathelper(ask2)
					}
					if(this.askType==2){
						this.websocketSend(ask?ask:params.ask)
					}
					this.form.ask = '';
				}
			});
		},
		chatClose() {
			if(this.askType==2){
				this.websocketOnclose();
			}
			this.chatFormVisible = false;
		},
		websocketOnmessage:function(e) {
			this.getChatList()
		},
		async goChat() {
			if(!localStorage.getItem('frontToken')) {
				this.toLogin();
				return;
			}
			await this.getChatList();
			this.askType = 1
			if(this.chatTimeChange()) {
				this.saveChathelper("您好，有什么可以帮您？");
			}
			this.chatFormVisible = true;
		},
		uploadSuccess(res) {
			if (res.code == 0) {
				this.askShow = !this.askShow;
				this.addChat('upload/' + res.file,2)
			}
		},
		uploadSuccess2(res) {
			if (res.code == 0) {
				this.askShow = !this.askShow;
				this.addChat('upload/' + res.file,3)
			}
		},
		uploadSuccess3(res) {
			if (res.code == 0) {
				this.askShow = !this.askShow;
				this.addChat('upload/' + res.file,4)
			}
		},
		download(url){
			if(!url){
				return false
			}
			window.open((location.href.split(this.$config.name).length>1 ? location.href.split(this.$config.name)[0] + this.$config.name + '/' + url :this.$config.baseUrl + url))
		},
		getChathelper(ask) {
			this.aiLoading = true
			let div = document.getElementsByClassName('chat-content')[0]
			console.log(div)
			setTimeout(() => {
				if (div){
					div.scrollTop = div.scrollHeight
				}
			}, 100)
			this.$http.post('deepseek/askai', {
				ask: `${ask}`,
			}).then(res => {
				if (res.data.code == 0) {
					this.aiLoading = false
					this.saveChathelper(res.data.data);
				}else {
					this.aiLoading = false
					this.saveChathelper(res.data.msg)
				}
			});
		},
		saveChathelper(reply) {
			this.$http.post('chat/save', {
				reply: reply,
				userid: Number(localStorage.getItem('frontUserid')),
				type: 1
			}).then(res => {
				if (res.data.code == 0) {
					this.form.ask = '';
					this.getChatList();
				}
			});
		},
		askChange() {
			this.askShow = !this.askShow;
			this.askType = this.askType == 1 ? 2 : 1
			if(this.askType==1) {
				if(this.chatTimeChange()) {
					this.saveChathelper("您好，有什么可以帮您？");
				}
				
				this.websocketOnclose();
			} else if(this.askType==2){
				if(this.chatTimeChange()) {
					this.saveChathelper('您好，在线客服很高兴为您服务！')
				}
				this.initWebSocket(1)
			}
		},
		menuShowClick4(index){
			this.showType4 = index
		},
		goMenu(path) {
			this.$router.push(path);
		},
		handleCommand(name){
			if(name == 'register') {
				this.logout()
			}
			else if (name == 'service') {
				this.goChat()
			}
			else if (name == 'user'){
				this.goMenu('/index/center')
			}
			else if (name == 'board'){
				this.goBoard()
			}
			else if (name == 'login'){
				this.toLogin()
			}
		},
		suoClick(){
			this.suoType = !this.suoType
			if(this.suoType){
				clearTimeout(this.showTimer)
			}else{
				this.showmouseover()
			}
		},
		showmouseover() {
			if(this.suoType){
				return false
			}
			let that = this
			clearTimeout(this.showTimer)
			this.showType = true
			this.showTimer = setTimeout(() => {
				that.$refs.aplayer.showList = false;
				that.showType = false

			}, 6000)
		},
		timeChange(e){
			let user = JSON.parse(localStorage.getItem('sessionForm'))
			if(e.target.currentTime>30&&this.audio[this.audioIndex].isfree==0&&(!user||!user.vip||(user.vip&&user.vip!='是'))){
				this.$refs.aplayer.pause()
				if(this.audioIndex==this.audio.length - 1){
					this.$store.state.app.audioIndex = 0
				}else{
					this.$store.state.app.audioIndex++
				}
			}
		},
		playing(e){
			for(let x in this.audio) {
				if(this.audio[x].id == this.$refs.aplayer.currentMusic.id) {
					this.$store.state.app.audioIndex = Number(x)
					break
				}
			}
		},
		getAplayerAudioEl() {
			const p = this.$refs.aplayer
			return p && p.$refs && p.$refs.audio ? p.$refs.audio : null
		},
		syncPlayerVolumeFromAudio() {
			const el = this.getAplayerAudioEl()
			if (!el) {
				return
			}
			this.playerVolumePct = Math.round((el.muted ? 0 : el.volume) * 100)
		},
		onExternalVolumeInput(e) {
			const pct = Math.max(0, Math.min(100, Number(e.target.value)))
			this.playerVolumePct = pct
			const el = this.getAplayerAudioEl()
			if (!el) {
				return
			}
			el.volume = pct / 100
			el.muted = pct === 0
		},
	}
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.top-el-dropdown-menu {
		border: 1px solid #EBEEF5;
		border-radius: 4px;
		padding: 10px 0;
		box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
		margin: 18px 0;
		background: #FFF;
		.service-item {
			border: 0;
			padding: 0 8px;
			margin: 0 10px;
			color: #333;
			background: none;
			width: auto;
			font-size: 14px;
			line-height: 32px;
			height: 32px;
			.icon {
				color: inherit;
				font-size: 14px;
			}
		}
		.service-item:hover {
			color: #0c588c;
			background: none;
		}
		.user-item {
			border: 0;
			padding: 0 8px;
			margin: 0 10px;
			color: #333;
			background: none;
			width: auto;
			font-size: 14px;
			line-height: 32px;
			height: 32px;
			.icon {
				color: inherit;
				font-size: 14px;
			}
		}
		.user-item:hover {
			color: #0c588c;
			background: none;
		}
		.board-item {
			border: 0;
			padding: 0 8px;
			margin: 0 10px;
			color: #333;
			background: none;
			width: auto;
			font-size: 14px;
			line-height: 32px;
			height: 32px;
			.icon {
				color: inherit;
				font-size: 14px;
			}
		}
		.board-item:hover {
			color: #0c588c;
			background: none;
		}
		.register-item {
			border: 0;
			padding: 0 8px;
			margin: 0 10px;
			color: #333;
			background: none;
			width: auto;
			font-size: 14px;
			line-height: 32px;
			height: 32px;
			.icon {
				color: inherit;
				font-size: 14px;
			}
		}
		.register-item:hover {
			color: #0c588c;
			background: none;
		}
	}
	.main-containers {
		.body-containers {
			padding: 0px 0 0;
			margin: 0;
			background: #fff;
			min-height: 100vh;
			position: relative;
			.top-container {
				padding: 0 7%;
				z-index: 1005;
				color: #333;
				display: flex;
				font-size: 16px;
				box-shadow: 0 0px 0px rgba(64, 158, 255, .3);
				top: 0;
				left: 0;
				background: #f6f6f6;
				width: 100%;
				justify-content: flex-end;
				align-items: center;
				position: relative;
				height: 50px;
				.top_title {
					margin: 0px auto 0 0;
					top: 130px;
					left: calc(7% + 20px);
					display: block;
					position: absolute;
					span {
						padding: 0;
						color: inherit;
						font-size: 20px;
						line-height: 44px;
						float: left;
					}
				}
				.top_tel {
					margin: 0 10px;
					color: inherit;
					font-size: inherit;
				}
				.dropdown-box {
					color: inherit;
					display: flex;
					font-size: inherit;
					.el-dropdown-link {
						display: flex;
						align-items: center;
						.top_avatar2 {
							border-radius: 100%;
							margin: 0 10px;
							object-fit: cover;
							display: inline-block;
							width: 36px;
							height: 36px;
						}
						.top_label2 {
							color: inherit;
							font-size: inherit;
							line-height: 32px;
						}
						.top_nickname2 {
							color: inherit;
							font-size: inherit;
							line-height: 32px;
						}
						.icon {
							margin: 0 0 0 5px;
							color: inherit;
							font-size: inherit;
						}
						.login-item {
							border: 0;
							padding: 0 8px;
							margin: 0 10px;
							color: inherit;
							background: none;
							width: auto;
							font-size: inherit;
							line-height: 32px;
							height: 32px;
							.icon {
								margin: 0 3px 0 0;
								color: inherit;
								font-size: inherit;
							}
						}
						.login-item:hover {
							cursor: pointer;
						}
					}
				}
			}
			.menu-preview {
				.el-scrollbar {
					height: 100%;
			  
					& ::v-deep .scrollbar-wrapper-vertical {
						overflow-x: hidden;
					}
			  
					& ::v-deep .scrollbar-wrapper-horizontal {
						overflow-y: hidden;
			  
						.el-scrollbar__view {
							white-space: nowrap;
						}
					}
				}
				border-radius: 20px;
				margin: 0 auto;
				z-index: 1002;
				color: #333;
				top: 100px;
				left: 7%;
				background: rgba(255,255,255,0.9);
				width: 86%;
				font-size: 16px;
				position: absolute;
				.menu-list {
					padding: 0 10px 0 20px;
					display: flex;
					justify-content: flex-end;
					position: relative;
					// 首页
					.menu-home {
						cursor: pointer;
						line-height: 100px;
						height: 100px;
						.title {
							border-radius: 6px 0 0 6px;
							padding: 0 10px;
							margin: 0 20px 0 0;
							color: #05441a;
							background: none;
							display: flex;
							.icon {
								padding: 0 10px;
								margin: 0;
								color: inherit;
								display: none;
								width: 24px;
								font-size: 24px;
							}
							.text {
								padding: 0 10px;
								color: inherit;
								white-space: nowrap;
								font-size: inherit;
							}
						}
					}
					.menu-home:hover {
						.title {
							color: #05441a;
						}
					}
					.menu-home.menu-active {
						.title {
							border-radius: 6px 0 0 6px;
							color: #05441a;
							background: none;
						}
					}
					// 其他盒子
					.menu-item {
						margin: 0 30px 0 0;
						color: #05441a;
						background: none;
						line-height: 100px;
						height: 100px;
						.title {
							cursor: pointer;
							padding: 0 0px;
							margin: 0 20px 0 0;
							display: flex;
							span {
								padding: 0 10px;
								margin: 0;
								color: inherit;
								display: none;
								width: 16px;
								font-size: inherit;
							}
							.text {
								padding: 0 0px;
								color: inherit;
								white-space: nowrap;
								font-size: inherit;
							}
						}
						.menu-child-list {
							margin: 0 0 0 -20px;
							z-index: 9999;
							flex-direction: column;
							background: rgba(255,255,255,.9);
							display: flex;
							width: 200px;
							justify-content: flex-start;
							position: absolute;
							flex-wrap: wrap;
							.child-item {
								cursor: pointer;
								padding: 0 20px;
								color: #333;
								width: 100% !important;
								font-size: 15px;
								line-height: 46px;
							}
							.child-item:hover {
								color: #fff;
								background: #05441a;
							}
						}
					}
					.menu-item:hover {
						.title {
							color: #05441a;
							background: none;
						}
					}
					.menu-item.menu-active {
						.title {
							color: #05441a;
							background: none;
						}
					}
				}
			}
			.banner-preview {
				padding: 0;
				margin: 0 auto;
				width: 100%;
				position: relative;
				height: 640px;
				.swiper-button-prev:after {
					display:none;
				}
				.swiper-button-next:after {
					display:none;
				}
				.swiper-slide {
					.swiper-item {
						width: 100%;
						height: 640px;
						.el-image {
							object-fit: cover;
							width: 100%;
							height: 640px;
						}
					}
				}
				@keyframes wave1 {from { left: -236px } to { left: -1233px }}
				@keyframes wave2 {from { left: 0 } to { left: -1009px }}
				.swiper-pagination {
					left: 0;
					bottom: 10px;
					width: 100%;
					::v-deep span.swiper-pagination-bullet {
						border-radius: 100%;
						margin: 0 4px;
						background: #000;
						display: inline-block;
						width: 8px;
						opacity: .2;
						height: 8px;
					}
					::v-deep span.swiper-pagination-bullet:hover {
						background: #fff;
						opacity: 1;
					}
					::v-deep span.swiper-pagination-bullet.swiper-pagination-bullet-active {
						background: #fff;
						opacity: 1;
					}
				}
				.swiper-button-next {
					margin: -12px 0 0;
					top: 50%;
					width: 24px;
					height: 24px;
					.icon {
						color: #fff;
						width: 24px;
						font-size: 24px;
						height: 24px;
					}
				}
				.swiper-button-prev {
					margin: -12px 0 0;
					top: 50%;
					width: 24px;
					height: 24px;
					.icon {
						color: #fff;
						width: 24px;
						font-size: 24px;
						height: 24px;
					}
				}
			}
			.bottom-preview {
				width: 100%;
				height: auto;
				.footer {
					padding: 20px 7%;
					color: #fff;
					display: flex;
					font-size: 16px;
					min-height: 100px;
					overflow: hidden;
					align-content: center;
					background: rgba(5, 68, 26,1);
					width: 100%;
					justify-content: center;
					align-items: center;
					text-align: center;
					height: auto;
				}
			}
		}
	}
	.chat-content {
		padding-bottom: 20px;
		width: 100%;
		margin-bottom: 10px;
		max-height: 600px;
		height: 600px;
		overflow-y: scroll;
		border: 1px solid #eeeeee;
		background: #fff;

		.left-content {
			float: left;
			margin-bottom: 10px;
			padding: 10px;
			max-width: 80%;
		}

		.right-content {
			float: right;
			margin-bottom: 10px;
			padding: 10px;
			max-width: 80%;
		}
	}

	.clear-float {
		clear: both;
	}
	.emoji-mart[data-v-7bc71df8] {
		font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
		display: -ms-flexbox;
		display: flex;
		-ms-flex-direction: column;
		flex-direction: column;
		height: 420px;
		color: #ffffff !important;
		border: 1px solid #d9d9d9;
		border-radius: 5px;
		background: #fff;
	}
	/* 隐藏播放器内置音量（喇叭 + 竖条），改用右下角悬浮音量 */
	.audioAnimation-box ::v-deep .aplayer-volume-wrap {
		display: none !important;
	}

	/* 默认仅显示圆形按钮，悬停 / 键盘聚焦时向上展开悬浮面板 */
	.audio-external-volume {
		position: absolute;
		right: 14px;
		bottom: 24px;
		z-index: 100000;
		display: flex;
		flex-direction: column-reverse;
		align-items: flex-end;
		gap: 0;
		pointer-events: auto;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
	}

	.audio-external-volume__trigger {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 30px;
		height: 30px;
		padding: 0;
		border: 1px solid rgba(0, 0, 0, 0.07);
		border-radius: 50%;
		background: rgba(255, 255, 255, 0.98);
		box-shadow: 0 1px 6px rgba(0, 0, 0, 0.08);
		cursor: pointer;
		transition: background 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
		backdrop-filter: blur(8px);
	}

	.audio-external-volume__trigger:hover {
		background: #fff;
		box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
		transform: scale(1.06);
	}

	.audio-external-volume__trigger:focus {
		outline: none;
	}

	.audio-external-volume__trigger:focus-visible {
		outline: 2px solid rgba(65, 184, 131, 0.5);
		outline-offset: 1px;
	}

	.audio-external-volume:hover .audio-external-volume__trigger,
	.audio-external-volume:focus-within .audio-external-volume__trigger {
		background: #fff;
		box-shadow: 0 3px 12px rgba(65, 184, 131, 0.22);
		border-color: rgba(65, 184, 131, 0.35);
	}

	.audio-external-volume__icon {
		display: flex;
		color: #4b5a6e;
		opacity: 0.92;
	}

	.audio-external-volume__panel {
		display: flex;
		align-items: center;
		gap: 10px;
		margin-bottom: 0;
		padding: 0 14px;
		max-height: 0;
		opacity: 0;
		overflow: hidden;
		border-radius: 100px;
		background: rgba(255, 255, 255, 0.97);
		border: 1px solid rgba(0, 0, 0, 0.06);
		box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12), 0 0 1px rgba(0, 0, 0, 0.04);
		pointer-events: none;
		transform: translateY(6px);
		transform-origin: bottom right;
		transition: max-height 0.28s ease, opacity 0.22s ease, padding 0.22s ease, transform 0.22s ease, box-shadow 0.22s ease;
		backdrop-filter: blur(10px);
	}

	.audio-external-volume:hover .audio-external-volume__panel,
	.audio-external-volume:focus-within .audio-external-volume__panel {
		max-height: 52px;
		opacity: 1;
		padding: 8px 14px;
		margin-bottom: 8px;
		pointer-events: auto;
		transform: translateY(0);
	}

	.audio-external-volume__slider {
		flex: 1;
		min-width: 0;
		width: 120px;
		display: flex;
		align-items: center;
	}

	.audio-external-volume__pct {
		flex-shrink: 0;
		min-width: 2.75em;
		text-align: right;
		font-size: 12px;
		font-weight: 600;
		font-variant-numeric: tabular-nums;
		color: #6b7c90;
		letter-spacing: 0.02em;
		user-select: none;
	}

	.audio-external-volume__range {
		-webkit-appearance: none;
		appearance: none;
		width: 100%;
		height: 20px;
		margin: 0;
		background: transparent;
		cursor: pointer;
		--track-h: 5px;
		--thumb-size: 14px;
		--accent: #41b883;
		--track-bg: #e4e8ec;
	}

	.audio-external-volume__range:focus {
		outline: none;
	}

	.audio-external-volume__range:focus-visible {
		outline: 2px solid rgba(65, 184, 131, 0.45);
		outline-offset: 3px;
		border-radius: 4px;
	}

	/* WebKit */
	.audio-external-volume__range::-webkit-slider-runnable-track {
		height: var(--track-h);
		border-radius: 100px;
		background: linear-gradient(to right, var(--accent) var(--vol), var(--track-bg) var(--vol));
	}

	.audio-external-volume__range::-webkit-slider-thumb {
		-webkit-appearance: none;
		appearance: none;
		width: var(--thumb-size);
		height: var(--thumb-size);
		margin-top: calc((var(--track-h) - var(--thumb-size)) / 2);
		border-radius: 50%;
		background: #fff;
		border: 2px solid var(--accent);
		box-shadow: 0 1px 4px rgba(0, 0, 0, 0.12);
		transition: transform 0.15s ease, box-shadow 0.15s ease;
	}

	.audio-external-volume__range:hover::-webkit-slider-thumb {
		transform: scale(1.08);
		box-shadow: 0 2px 8px rgba(65, 184, 131, 0.35);
	}

	.audio-external-volume__range:active::-webkit-slider-thumb {
		transform: scale(1.12);
	}

	/* Firefox */
	.audio-external-volume__range::-moz-range-track {
		height: var(--track-h);
		border-radius: 100px;
		background: var(--track-bg);
	}

	.audio-external-volume__range::-moz-range-progress {
		height: var(--track-h);
		border-radius: 100px 0 0 100px;
		background: var(--accent);
	}

	.audio-external-volume__range::-moz-range-thumb {
		width: var(--thumb-size);
		height: var(--thumb-size);
		border-radius: 50%;
		background: #fff;
		border: 2px solid var(--accent);
		box-shadow: 0 1px 4px rgba(0, 0, 0, 0.12);
		cursor: pointer;
	}
</style>
