<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'→'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/xingyezixun?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item3"><a href="javascript:void(0);">详情</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-fanhui01"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="detail-preview">
			<div class="attr">
				<div class="info">
					<div class="title-item">
						<div class="detail-title">
							{{detail.zixunbiaoti}}
						</div>
						<div class="colectBtn" @click="storeup(1)" v-show="!isStoreup">
							<i class="icon iconfont icon-shoucang10"></i>
							<span class="text">收藏({{detail.storeupnum}})</span>
						</div>
						<div class="colectBtn colectBtnActive" @click="storeup(-1)" v-show="isStoreup">
							<i class="icon iconfont icon-shoucang12"></i>
							<span class="text">已收藏({{detail.storeupnum}})</span>
						</div>
					</div>
					<div class="item">
						<div class="lable">资讯分类</div>
						<div class="text "  >{{detail.zixunfenlei}}</div>
					</div>
					<div class="item">
						<div class="lable">发布人</div>
						<div class="text "  >{{detail.faburen}}</div>
					</div>
					<div class="item">
						<div class="lable">发布时间</div>
						<div class="text "  >{{detail.fabushijian}}</div>
					</div>
					<div class="item">
						<div class="lable">简介</div>
						<div class="text "  >{{detail.jianjie}}</div>
					</div>
					<div class="item">
						<div class="lable">点击次数</div>
						<div class="text "  >{{detail.clicknum}}</div>
					</div>
					<div class="item">
						<div class="lable">评分</div>
						<div class="text "  >{{detail.totalscore}}</div>
					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('xingyezixun','修改')" @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('xingyezixun','删除')" @click="delClick">删除</el-button>
						<el-button class="reserveBtn" 
							v-if="btnAuth('xingyezixun','解读')" 
							@click="onAcross('zixunjiedu','','','','')" type="warning">
							解读
						</el-button>
						<el-button class="editBtn" @click="allchapterClick()" type="warning" v-if="btnAuth('xingyezixun','章节管理')">章节管理</el-button>
						<el-button class="editBtn" @click="discussClick()" type="warning" v-if="btnAuth('xingyezixun','查看评论')">查看评论</el-button>
					</div>
				</div>
			</div>
		
			<div class="detail-swpier2" v-if="detailBanner.length">
				<div class="swiper21">
					<div class="swiper-container mySwiper21">
						<div class="swiper-wrapper">
							<div class="swiper-slide" v-for="item in detailBanner" :key="item.id">
								<div class="swiper-item">
									<img v-if="item.substr(0,4)=='http'" :src="item" class="image">
									<img v-else :src="baseUrl + item" class="image">
								</div>
							</div>
						</div>
						<div class="swiper-button-prev">
							<span class="icon iconfont icon-jiantou39"></span>
						</div>
						<div class="swiper-button-next">
							<span class="icon iconfont icon-jiantou18"></span>
						</div>
					</div>
				</div>
				<div class="swiper22">
					<div class="swiper-container mySwiper22">
						<div class="swiper-wrapper">
							<div class="swiper-slide" v-for="item in detailBanner" :key="item.id">
								<div class="swiper-item">
									<img v-if="item.substr(0,4)=='http'" :src="item" class="image">
									<img v-else :src="baseUrl + item" class="image">
								</div>
							</div>
						</div>
						<div class="swiper-button-prev">
							<span class="icon iconfont icon-jiantou39"></span>
						</div>
						<div class="swiper-button-next">
							<span class="icon iconfont icon-jiantou18"></span>
						</div>
					</div>
				</div>
			</div>

			<div class="zancai">
				<div v-if="!isThumbsupnum && !isCrazilynum" class="zan" @click="thumbsupOrCrazily(21)">
					<i class="icon iconfont icon-zan07"></i>
					<span class="text">赞一下({{detail.thumbsupnum}})</span>
				</div>
				<div v-if="!isThumbsupnum && !isCrazilynum" class="cai" @click="thumbsupOrCrazily(22)">
					<i class="icon iconfont icon-cai01"></i>
					<span class="text">踩一下({{detail.crazilynum}})</span>
				</div>
				<div v-if="isThumbsupnum" class="zanActive" @click="cancelThumbsupOrCrazily(21)">
					<i class="icon iconfont icon-zan11"></i>
					<span class="text">已赞({{detail.thumbsupnum}})</span>
				</div>
				<div v-if="isCrazilynum" class="caiActive" @click="cancelThumbsupOrCrazily(22)">
					<i  class="icon iconfont icon-cai16"></i>
					<span class="text">已踩({{detail.crazilynum}})</span>
				</div>
			</div>


			<el-tabs id="tabsBox" class="detail-tabs" v-model="activeName" type="border-card" v-if="tabsNum>0" >
				<el-tab-pane label="资讯内容" name="1">
					<div class="ql-snow ql-editor" v-html="detail.zixunneirong"></div>
				</el-tab-pane>
				<el-tab-pane label="评论" name="2">
					<el-form class="add commentForm" :model="form" :rules="rules" ref="form">
						<el-form-item class="item" label="评论" prop="content">
							<editor
								myQuillEditor="content"
								v-model="form.content" 
								class="editor" 
								action="file/upload">
							</editor>
						</el-form-item>
						<el-form-item class="item" label="评分" prop="score">
							<el-rate
								v-model="form.score"
								:max='Number(5)'
								:allow-half='false'
								:low-threshold='Number(2)'
								:high-threshold='Number(4)'
								:show-text='false'
								:texts='["极差", "失望", "一般", "满意", "惊喜"]'
								text-color='#1F2D3D'
								:colors='["#F7BA2A", "#F7BA2A", "#F7BA2A"]'
								void-color='#C6D1DE'
								disabled-void-color='#EFF2F7'
								:icon-classes='["el-icon-star-on", "el-icon-star-on","el-icon-star-on"]'
								void-icon-class='el-icon-star-off'
								disabled-void-icon-class='el-icon-star-on'
								:show-score='false'
							>
							</el-rate>
						</el-form-item>
						<el-form-item class="commentBtn">
							<el-button class="submitBtn" type="primary" @click="submitForm('form')">立即提交</el-button>
							<el-button class="resetBtn" @click="resetForm('form')">重置</el-button>
						</el-form-item>
					</el-form>
				
					<div v-if="infoList.length" class="comment-list">
						<div class="comment-item" v-for="item in infoList" :key="item.id" @mouseenter="discussEnter(item.id)" :id="'discuss' + item.id"
							@mouseleave="discussLeave">
							<div class="istop" v-if="item.istop">
								<span class="icon iconfont icon-jiantou24"></span>
							</div>
							<div class="user">
								<el-image v-if="item.avatarurl" :size="50" :src="baseUrl + item.avatarurl"></el-image>
								<el-image v-if="!item.avatarurl" :size="50" :src="require('@/assets/touxiang.png')"></el-image>
								<div class="name">{{item.nickname}}</div>
							</div>
							<div class="comment-content-box">
								<div class="ql-snow ql-editor" v-html="item.content"></div>
								<el-rate
									v-model="item.score"
									disabled
									:max='Number(5)'
									:allow-half='false'
									:low-threshold='Number(2)'
									:high-threshold='Number(4)'
									:show-text='false'
									:texts='["极差", "失望", "一般", "满意", "惊喜"]'
									text-color='#1F2D3D'
									:colors='["#F7BA2A", "#F7BA2A", "#F7BA2A"]'
									void-color='#C6D1DE'
									disabled-void-color='#EFF2F7'
									:icon-classes='["el-icon-star-on", "el-icon-star-on","el-icon-star-on"]'
									void-icon-class='el-icon-star-off'
									disabled-void-icon-class='el-icon-star-on'
									:show-score='false'
								>
								</el-rate>
								<div class="comment-time">{{item.addtime}}</div>
								<div class="zancai-box">
									<div v-if="!comcaiChange(item)" class="zan-item" :class="comzanChange(item)?'active':''" @click="comzanClick(item)">
										<span class="icon iconfont" :class="comzanChange(item)?'icon-zan11':'icon-zan07'"></span>
										<span class="label">{{comzanChange(item)?'已赞':'赞'}}</span>
										<span class="num">({{item.thumbsupnum}})</span>
									</div>
									<div v-if="!comzanChange(item)" class="cai-item" :class="comcaiChange(item)?'active':''" @click="comcaiClick(item)">
										<span class="icon iconfont" :class="comcaiChange(item)?'icon-cai16':'icon-cai01'"></span>
										<span class="label">{{comcaiChange(item)?'已踩':'踩'}}</span>
										<span class="num">({{item.crazilynum}})</span>
									</div>
								</div>
								<div class="comment-btn">
									<!-- <el-button :style='{"border":"0","cursor":"pointer","padding":"0 20px","margin":"0 10px","outline":"none","color":"#fff","borderRadius":"2px","background":"#05441a","width":"auto","lineHeight":"34px","fontSize":"14px","height":"34px"}'>回复</el-button> -->
									<el-button class="delBtn" v-if="showIndex==item.id&&userid==item.userid" @click="discussDel(item.id)">删除</el-button>
								</div>
							</div>
							<div class="comment-content-box" v-if="item.reply">
								回复：<span class="ql-snow ql-editor" v-html="item.reply"></span>
							</div>
						</div>
					</div>
				
					<el-pagination
						background
						id="pagination" class="pagination"
						:page-size="pageSize"
						prev-text="<"
						next-text=">"
						:hide-on-single-page="true"
						:layout='["total","prev","pager","next","sizes","jumper"].join()'
						:total="total"
						@current-change="curChange"
						@prev-click="prevClick"
						@next-click="nextClick"
						@size-change="sizeChange"
						></el-pagination>
				</el-tab-pane>
			</el-tabs>

		</div>
	</div>
</template>

<script>
	import axios from 'axios'
	import Swiper from "swiper";
	export default {
		//数据集合
		data() {
			return {
				tablename: 'xingyezixun',
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '行业资讯'
					}
				],
				title: '',
				detailBanner: [],
				userid: Number(localStorage.getItem('frontUserid')),
				id: 0,
				detail: {},
				tabsNum: 2,
				activeName: '1',
				form: {
					content: '',
					userid: Number(localStorage.getItem('frontUserid')),
					nickname: localStorage.getItem('username'),
					avatarurl: '',
					score: 0,
				},
				showIndex: -1,
				infoList: [],
				colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
				rules: {
					content: [
						{ required: true, message: '请输入内容', trigger: 'blur' }
					],
					score: [
						{ required: true, message: '请选择评分', trigger: 'blur' }
					],
				},
				total: 1,
				pageSize: 10,
				totalPage: 1,
				storeupParams: {
					name: '',
					picture: '',
					refid: 0,
					tablename: 'xingyezixun',
					userid: Number(localStorage.getItem('frontUserid'))
				},
				isStoreup: false,
				storeupInfo: {},
				isCrazilynum: false,
				isThumbsupnum: false,
				thumbsupOrCrazilyInfo: {},
				buynumber: 1,
				centerType: false,
				storeupType: false,
			}
		},
		created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0) {
				this.centerType = true
			}
			if(this.$route.query.storeupType&&this.$route.query.storeupType!=0) {
				this.storeupType = true
			}
			this.init();
		},
		mounted() {
			setTimeout(()=>{
				let mySwiper22 = new Swiper(".mySwiper22", {"navigation":{"nextEl":".swiper-button-next","prevEl":".swiper-button-prev"},"freeMode":true,"watchSlidesVisibility":true,"watchSlidesProgress":true,"loopedSlides":6,"slidesPerView":3,"spaceBetween":10})
				let option21 = {...{"navigation":{"nextEl":".swiper-button-next","prevEl":".swiper-button-prev"},"loopedSlides":5,"spaceBetween":10}}
				option21.thumbs = {
					swiper: mySwiper22
				}
				new Swiper(".mySwiper21", option21)
			},100)
		},
		computed: {
			username() {
				return localStorage.getItem('username')
			},
			frontSessionTable() {
				return localStorage.getItem('frontSessionTable')
			},
		},
		//方法集合
		methods: {
			init() {
				this.id = this.$route.query.id
				this.baseUrl = this.$config.baseUrl;
				this.$http.get(this.tablename + '/detail/'  + this.id, {}).then(async res => {
					if (res.data.code == 0) {
						this.detail = res.data.data;
						this.title = this.detail.zixunbiaoti;
						if(this.detail.fengmian) {
							this.detailBanner = this.detail.fengmian.split(",w").length>1?[this.detail.fengmian]:this.detail.fengmian.split(',');
						}
						this.$forceUpdate();
						this.getDiscussList(1);
						if(localStorage.getItem('frontToken')){
							this.getStoreupStatus();
							this.getThumbsupOrCrazilyStatus();
						}

					}
				});
			},
			async onAcross(acrossTable,crossOptAudit,crossOptPay,statusColumnName,tips,statusColumnValue,type=1){
				localStorage.setItem('crossTable',`xingyezixun`);
				localStorage.setItem('crossObj', JSON.stringify(this.detail));
				localStorage.setItem('statusColumnName',statusColumnName);
				localStorage.setItem('statusColumnValue',statusColumnValue);
				localStorage.setItem('tips',tips);
				if(statusColumnName!=''&&!statusColumnName.startsWith("[")) {
					var obj = JSON.parse(localStorage.getItem('crossObj'));
					for (var o in obj){
						if(o==statusColumnName && obj[o]==statusColumnValue){
							this.$message({
								type: 'error',
								message: tips,
								duration: 1500
							});
							return
						}
					}
				}
				this.$router.push({path: '/index/' + acrossTable + 'Add', query: {type: 'cross'}});
			},
			storeup(type) {
				if (type == 1 && !this.isStoreup) {
					this.storeupParams.name = this.title;
					this.storeupParams.picture = this.detailBanner[0];
					this.storeupParams.refid = this.detail.id;
					this.storeupParams.type = String(type);
					this.$http.post('storeup/add', this.storeupParams).then(res => {
						if (res.data.code == 0) {
							this.isStoreup = true;
							this.detail.storeupnum++
							this.$http.post('xingyezixun/update', this.detail).then(res => {});
							this.$message({
								type: 'success',
								message: '收藏成功!',
								duration: 1500,
							});
						}
					});
				}
				if (type == -1 && this.isStoreup) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '1', refid: this.detail.id, tablename: 'xingyezixun', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isStoreup = true;
							this.storeupInfo = res.data.data.list[0];
							let delIds = new Array();
							delIds.push(this.storeupInfo.id);
							this.$http.post('storeup/delete', delIds).then(res => {
								if (res.data.code == 0) {
									this.isStoreup = false;
									this.detail.storeupnum--
									this.$http.post('xingyezixun/update', this.detail).then(res => {});
									this.$message({
										type: 'success',
										message: '取消成功!',
										duration: 1500,
									});
								}
							});
						}
					});
				}
			},
			getStoreupStatus(){
				if(localStorage.getItem("frontToken")) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '1', refid: this.detail.id, tablename: 'xingyezixun', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isStoreup = true;
							this.storeupInfo = res.data.data.list[0];
						}
					});
				}
			},
			async thumbsupOrCrazily(type) {
				this.storeupParams.name = this.title;
				this.storeupParams.picture = this.detailBanner[0];
				this.storeupParams.refid = this.detail.id;
				this.storeupParams.type = String(type);
				await this.$http.post('storeup/add', this.storeupParams).then(res => {
					if (res.data.code == 0) {
						let detail = JSON.parse(JSON.stringify(this.detail))
						if (type == 21) detail.thumbsupnum = Number(detail.thumbsupnum) + 1;
						if (type == 22) detail.crazilynum = Number(detail.crazilynum) + 1;
						this.$http.post('xingyezixun/update', detail).then(res => {
							this.detail = detail
						});
						this.getThumbsupOrCrazilyStatus();
						this.$message({
							type: 'success',
							message: '操作成功!',
							duration: 1500,
						});
						
					}
				});
				
			},
			async cancelThumbsupOrCrazily(type) {
				let delIds = new Array();
				delIds.push(this.thumbsupOrCrazilyInfo.id);
				await this.$http.post('storeup/delete', delIds).then(res => {
					if (res.data.code == 0) {
						let detail = JSON.parse(JSON.stringify(this.detail))
						if (type == 21) detail.thumbsupnum -= 1;
						if (type == 22) detail.crazilynum -= 1;
						this.$http.post('xingyezixun/update', detail).then(res => {
							this.detail = detail
						});
						this.isThumbsupnum = false;
						this.isCrazilynum = false;
						this.$message({
							type: 'success',
							message: '取消成功!',
							duration: 1500,
						});
					}
				});
				
			},
			getThumbsupOrCrazilyStatus() {
				if(localStorage.getItem("frontToken")) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '21', refid: this.detail.id, tablename: 'xingyezixun', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isThumbsupnum = true;
							this.thumbsupOrCrazilyInfo = res.data.data.list[0];
						}
					});
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '22', refid: this.detail.id, tablename: 'xingyezixun', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isCrazilynum = true;
							this.thumbsupOrCrazilyInfo = res.data.data.list[0];
						}
					});
				}
			},
			curChange(page) {
				this.getDiscussList(page);
			},
			prevClick(page) {
				this.getDiscussList(page);
			},
			nextClick(page) {
				this.getDiscussList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getDiscussList(1);
			},
			// 返回按钮
			backClick(){
				if(this.storeupType){
					history.back()
				}else{
					let params = {}
					if(this.centerType){
						params.centerType = 1
					}
					this.$router.push({path: '/index/xingyezixun', query: params});
				}
			},
			// 下载
			download(file ){
				if(!file) {
					this.$message({
						type: 'error',
						message: '文件不存在',
						duration: 1500,
					});
					return;
				}
				let arr = file.replace(new RegExp('upload/', "g"), "")
				axios.get(this.baseUrl + 'file/download?fileName=' + arr, {
					headers: {
						token: localStorage.getItem("frontToken")
					},
					responseType: "blob"
				}).then(({
					data
				}) => {
					const binaryData = [];
					binaryData.push(data);
					const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
						type: 'application/pdf;chartset=UTF-8'
					}))
					const a = document.createElement('a')
					a.href = objectUrl
					a.download = arr
					// a.click()
					// 下面这个写法兼容火狐
					a.dispatchEvent(new MouseEvent('click', {
						bubbles: true,
						cancelable: true,
						view: window
					}))
					window.URL.revokeObjectURL(data)
				},err=>{
					axios.get((location.href.split(this.$config.name).length>1 ? location.href.split(this.$config.name)[0] :'') + this.$config.name + 'file/download?fileName=' + arr, {
						headers: {
							token: localStorage.getItem("frontToken")
						},
						responseType: "blob"
					}).then(({
						data
					}) => {
						const binaryData = [];
						binaryData.push(data);
						const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
							type: 'application/pdf;chartset=UTF-8'
						}))
						const a = document.createElement('a')
						a.href = objectUrl
						a.download = arr
						// a.click()
						// 下面这个写法兼容火狐
						a.dispatchEvent(new MouseEvent('click', {
							bubbles: true,
							cancelable: true,
							view: window
						}))
						window.URL.revokeObjectURL(data)
					})
				})
			},
			getDiscussList(page,type=1) {
				this.$http.get('discussxingyezixun/list', {
					params: {
						page, 
						limit: this.pageSize, 
						refid: this.detail.id,
						sort: 'istop',
						order: 'desc',
					}
				}).then(res => {
					if (res.data.code == 0) {
						for(let x in res.data.data.list) {
							res.data.data.list[x].content = res.data.data.list[x].content.replace(/img src/gi,"img style=\"width:30%;\" src");
						}
						this.infoList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(type==1) {
							if(this.$route.query.discussId&&this.$route.query.discussId!=0) {
								this.$nextTick(()=>{
									document.getElementById('discuss' + this.$route.query.discussId).scrollIntoView({
										behavior: 'smooth'
									});
								})
							}
						}
					}
				});
			},
			comzanChange(row){
				if(row.tuserids){
					let arr = row.tuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							return true
						}
					}
				}
				return false
			},
			comzanClick(row){
				if(!this.userid){
					return false
				}
				if(!this.comzanChange(row)){
					row.thumbsupnum++
					if(row.tuserids){
						row.tuserids = row.tuserids + ',' + this.userid
					}else {
						row.tuserids = String(this.userid)
					}
					this.$http.post('discussxingyezixun/update',row).then(rs=>{
						this.$message.success('点赞成功')
					})
				}else {
					row.thumbsupnum--
					let arr = row.tuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							arr.splice(x,1)
						}
					}
					row.tuserids = arr.join(',')
					this.$http.post('discussxingyezixun/update',row).then(rs=>{
						this.$message.success('取消成功')
					})
				}
			},
			comcaiChange(row){
				if(row.cuserids){
					let arr = row.cuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							return true
						}
					}
				}
				return false
			},
			comcaiClick(row){
				if(!this.userid){
					return false
				}
				if(!this.comcaiChange(row)){
					row.crazilynum++
					if(row.cuserids){
						row.cuserids = row.cuserids + ',' + this.userid
					}else {
						row.cuserids = String(this.userid)
					}
					this.$http.post('discussxingyezixun/update',row).then(rs=>{
						this.$message.success('点踩成功')
					})
				}else {
					row.crazilynum--
					let arr = row.cuserids.split(',')
					for(let x in arr){
						if(arr[x] == this.userid){
							arr.splice(x,1)
						}
					}
					row.cuserids = arr.join(',')
					this.$http.post('discussxingyezixun/update',row).then(rs=>{
						this.$message.success('取消成功')
					})
				}
			},
			discussEnter(index){
				this.showIndex = index
			},
			discussLeave(){
				this.showIndex = -1
			},
			discussDel(id){
				this.$confirm('是否删除此评论？').then(_ => {
					this.$http.post('discussxingyezixun/delete',[id]).then(res=>{
						if(res.data&&res.data.code==0){
							this.addDiscussNum(1)
							this.$message({
								type: 'success',
								message: '删除成功!',
								duration: 1500,
								onClose: () => {
									this.getDiscussList(1);
								}
							});
						}
					})
				}).catch(_ => {});
			},
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.$http.get('discussxingyezixun/page',{params: {
							page: 1,
							limit: 1,
							refid: this.detail.id,
							userid: Number(localStorage.getItem('frontUserid'))
						}}).then(rs=>{
							if(rs.data.data.list.length){
								this.$message({
									type: 'error',
									message: '每个用户只能评论一次!',
									duration: 1500
								});
								return false
							}
							this.addComments()
						})
					} else {
						return false;
					}
				});
			},
			addComments(content=null,type=1) {
				let data = JSON.parse(JSON.stringify(this.form))
				data.refid = this.detail.id;
				data.avatarurl = localStorage.getItem('frontHeadportrait')?localStorage.getItem('frontHeadportrait'):'';
				if(type==2) {
					data.content = content
				}
				this.$http.post('discussxingyezixun/add', data).then(rs2 => {
					if (rs2.data.code == 0) {
						if(type==1) {
							this.form.content = '';
							this.form.score = 0
						}
						this.addDiscussNum(2)
						this.getDiscussList(1,type);
						this.$message({
							type: 'success',
							message: '评论成功!',
							duration: 1500,
						});
					}
				});
			},
			resetForm(formName) {
				this.$refs[formName].resetFields();
			},
			addDiscussNum(type){
				if(type==2){
					this.detail.discussnum++
				}else if(type==1){
					if(this.detail.discussnum!=0){
						this.detail.discussnum--
					}else{
						this.detail.discussnum = 0
					}
				}
				this.$http.get('discussxingyezixun/list',{params: {
					page: 1,
					limit: 10000,
					refid: this.detail.id,
				}}).then(rs=>{
					let score = 0
					for(let x in rs.data.data.list){
						score += Number(rs.data.data.list[x].score)
					}
					this.detail.totalscore = rs.data.data.list.length?Number((score / Number(rs.data.data.list.length)).toFixed(2)):0
					this.$http.post('xingyezixun/update',this.detail).then(res=>{})
				})
			},


			// 权限判断
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			// 修改
			editClick(){
				this.$router.push(`/index/xingyezixunAdd?type=edit&&id=${this.detail.id}`);
			},
			// 删除
			async delClick(){
				await this.$confirm('是否删除此行业资讯？') .then(_ => {
					this.$http.post('xingyezixun/delete', [this.detail.id]).then(async res => {
						if (res.data.code == 0) {
							this.$http.get('storeup/list',{params:{
								page: 1,
								limit: 100,
								refid: this.detail.id,
								tablename: 'xingyezixun',
							}}).then(async obj=>{
								if(obj.data&&obj.data.code==0){
									let arr = []
									for(let x in obj.data.data.list){
										arr.push(obj.data.data.list[x].id)
									}
									if(arr.length){
										await this.$http.post('storeup/delete',arr).then(()=>{})
									}
									this.$message({
										type: 'success',
										message: '删除成功!',
										duration: 1500,
										onClose: () => {
											history.back()
										}
									});
								}
							})
						}
					});
				}).catch(_ => {});
			},
			allchapterClick (){
				let params = {
					refid: this.detail.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/chapterxingyezixun', query: params});
			},
			discussClick (){
				let params = {
					refid: this.detail.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/discussxingyezixun', query: params});
			},
			// 获取uuid
			getUUID() {
				return new Date().getTime();
			},
		},
		components: {
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.detail-preview {
		padding: 0 7%;
		margin: 0px auto;
		background: #f9f9f9;
		display: flex;
		width: 100%;
		position: relative;
		flex-wrap: wrap;
		.attr {
			padding: 0px;
			margin: 0 0 20px;
			background: none;
			flex: 1;
			display: flex;
			position: relative;
			order: 1;
			.info {
				border-radius: 0px;
				padding: 10px;
				margin: 0;
				background: #fff;
				flex: 1;
				.title-item {
					border: 0px solid #eee;
					padding: 10px;
					margin: 0 0 10px 0;
					background: none;
					display: flex;
					justify-content: space-between;
					align-items: center;
					.detail-title {
						padding: 0;
						color: #333;
						font-weight: 600;
						font-size: 22px;
						border-color: #009899;
						border-width: 0 0 0 0px;
						line-height: 1;
						border-style: solid;
					}
					.colectBtn {
						cursor: pointer;
						border: 0px solid #eee;
						border-radius: 20px;
						padding: 5px 15px;
						background: #fff;
						.icon {
							color: #666;
							font-size: 16px;
						}
						.text {
							color: #666;
							font-size: 16px;
						}
					}
					.colectBtnActive {
						background: #f60;
						border-color: #f60;
						.icon {
							color: #fff;
							font-size: 16px;
						}
						.text {
							color: #fff;
							font-size: 16px;
						}
					}
					.colectBtn:hover {
						background: #f60;
						border-color: #f60;
						.icon {
							color: #fff;
						}
						.text {
							color: #fff;
						}
					}
					.colectBtnActive:hover {
						background: #f60;
						border-color: #f60;
						.icon {
							color: #fff;
						}
						.text {
							color: #fff;
						}
					}
				}
				.item {
					padding: 0 10px;
					margin: 0 0 10px 0;
					background: none;
					display: flex;
					justify-content: spaceBetween;
					.lable {
						padding: 0 10px 0 0;
						color: #333;
						white-space: nowrap;
						font-weight: 500;
						width: auto;
						font-size: 16px;
						line-height: 24px;
						text-align: right;
						height: auto;
					}
					.count-down {
						padding: 0 10px;
						color: #666;
						word-break: break-all;
						flex: 1;
						font-size: 14px;
						line-height: 24px;
						height: auto;
					}
					.text {
						padding: 0 10px;
						color: #666;
						word-break: break-all;
						flex: 1;
						font-size: 14px;
						line-height: 24px;
						height: auto;
					}
					.bold {
						font-weight: bold;
					}
					.link {
						cursor: pointer;
						text-decoration: underline;
					}
				}
				.item-price {
					.lable {
					}
					.text {
					}
				}
				.btn_box {
					padding: 10px 0;
					display: flex;
					flex-wrap: wrap;
				}
				.editBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0px;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: rgba(64, 158, 255, 1);
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.editBtn:hover {
					opacity: 0.7;
				}
				.delBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0px;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: rgba(255, 0, 0, 1.0);
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.delBtn:hover {
					opacity: 0.7;
				}
			}
		}
		.detail-swpier2 {
			margin: 0 0 20px 20px;
			width: 480px;
			height: 480px;
			order: 2;
			.swiper21 {
				width: 100%;
				height: auto;
				.swiper-button-prev:after {
					display:none;
				}
				.swiper-button-next:after {
					display:none;
				}
				.swiper-item {
					width: 100%;
					height: auto;
					img {
						object-fit: cover;
						width: 100%;
						height: 400px;
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
			}
			.swiper22 {
				width: 100%;
				height: auto;
				
				.swiper-button-prev:after {
					display:none;
				}
				.swiper-button-next:after {
					display:none;
				}
				
				.swiper-item {
					width: 100%;
					opacity: 0.4;
					height: auto;
					img {
						object-fit: cover;
						width: 100%;
						height: 100px;
					}
				}
				.swiper-slide.swiper-slide-thumb-active div {
					opacity: 1;
				}
				.swiper-button-prev {
					margin: -7px 0 0;
					top: 50%;
					width: 14px;
					height: 14px;
					.icon {
						color: #fff;
						width: 14px;
						font-size: 14px;
						height: 14px;
					}
				}
				.swiper-button-next {
					margin: -7px 0 0;
					top: 50%;
					width: 14px;
					height: 14px;
					.icon {
						color: #fff;
						width: 14px;
						font-size: 14px;
						height: 14px;
					}
				}
			}
		}
		.zancai {
			padding: 0;
			margin: 0px auto 20px;
			background: none;
			display: flex;
			width: 100%;
			justify-content: center;
			order: 3;
			.zan {
				cursor: pointer;
				border: 0px solid #ddd;
				border-radius: 4px;
				padding: 10px 20px;
				margin: 0 100px 0 0;
				background: #fff;
				display: flex;
				width: auto;
				justify-content: center;
				align-items: center;
				.icon {
					margin: 0 3px;
					color: #666;
					font-size: 14px;
				}
				.text {
					margin: 0 3px;
					color: #666;
					font-size: 16px;
				}
			}
			.zan:hover {
				background: #05441a;
				border-color: #05441a;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.zanActive {
				background: #05441a;
				border-color: #05441a;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.zanActive:hover {
				background: #05441a;
				border-color: #05441a;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			
			.cai {
				cursor: pointer;
				border: 0px solid #ddd;
				border-radius: 4px;
				padding: 10px 20px;
				margin: 0;
				background: #fff;
				display: flex;
				width: auto;
				justify-content: center;
				align-items: center;
				.icon {
					margin: 0 3px;
					color: #666;
					font-size: 14px;
				}
				.text {
					margin: 0 3px;
					color: #666;
					font-size: 16px;
				}
			}
			.cai:hover {
				background: #05441a;
				border-color: #05441a;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.caiActive {
				background: #05441a;
				border-color: #05441a;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.caiActive:hover {
				background: #05441a;
				border-color: #05441a;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
		}
		.detail-tabs {
			border: 0px solid #DCDFE6;
			box-shadow: none;
			padding: 10px;
			margin: 20px auto;
			background: #fff;
			width: 100%;
			order: 5;
			& ::v-deep .el-tabs__header .el-tabs__nav-wrap {
				margin-bottom: 0;
			}
			::v-deep .el-tabs__header {
				padding: 8px 20px 0;
				background: #fff;
				display: block;
				width: 100%;
				border-color: #eee;
				border-width: 0 0 1px;
				line-height: 1.5;
				border-style: solid;
				text-align: center;
			}
			
			::v-deep .el-tabs__header .el-tabs__item {
				border: 0;
				padding: 0 0px;
				margin: 0 30px 0 0;
				color: #333;
				font-weight: 500;
				display: inline-block;
				font-size: 18px;
				border-color: #fff;
				line-height: 40px;
				background: none;
				border-width: 0 0 2px;
				position: relative;
				border-style: solid;
				list-style: none;
				height: 40px;
			}
			
			::v-deep .el-tabs__header .el-tabs__item:hover {
				color: #05441a;
				background: none;
				border-color: #05441a;
			}
			
			::v-deep .el-tabs__header .el-tabs__item.is-active {
				margin: 0 30px 0 0;
				color: #05441a;
				background: none;
				font-size: 18px;
				border-color: #05441a;
			}
			
			::v-deep .el-tabs__content {
				padding: 15px 20px;
				background: #fff;
				width: 100%;
				font-size: 16px;
			}
			.commentForm {
				box-shadow: none;
				padding: 0px;
				margin: 20px 0 20px;
				width: 100%;
				.item {
					display: flex;
					width: 100%;
					justify-content: flex-start;
					align-items: center;
					height: auto;
					::v-deep .el-form-item__label {
						padding: 0 10px 0 0;
						color: #666;
						white-space: nowrap;
						width: auto;
						font-size: 16px;
						line-height: 1.5;
						text-align: left;
					}
					.editor {
						border: 0px solid #ddd;
						border-radius: 4px;
						box-shadow: none;
						outline: none;
						color: #333;
						flex: 1;
						width: 100%;
						font-size: 14px;
						line-height: 32px;
						::v-deep .avatar-uploader {
							height: 0;
							line-height: 0;
						}
					}
					.editor ::v-deep .ql-toolbar {
						background: none;
					}
					.editor ::v-deep .ql-container {
						background: none;
						min-height: 180px;
					}
					.editor ::v-deep .ql-container .ql-blank::before {
						color: #999;
					}
				}
				.commentBtn {
					padding: 0;
					margin: 10px 0 0;
					width: 100%;
					text-align: left;
					height: auto;
					.submitBtn {
						border: 0;
						cursor: pointer;
						border-radius: 2px;
						padding: 0 20px;
						margin: 0 20px 0 0;
						outline: none;
						color: #fff;
						background: #05441a;
						width: auto;
						font-size: 15px;
						line-height: 40px;
						height: 40px;
					}
					.submitBtn:hover {
						opacity: 0.7;
					}
					.resetBtn {
						border: 0px solid #4789d450;
						cursor: pointer;
						padding: 0 20px;
						margin: 0 20px 0 0;
						color: #fff;
						font-size: 14px;
						line-height: 40px;
						border-radius: 2px;
						outline: none;
						background: #999;
						width: auto;
						min-width: 100px;
						height: 40px;
					}
					.resetBtn:hover {
						opacity: 0.8;
					}
				}
			}
			.comment-list {
				box-shadow: none;
				padding: 0px;
				margin: 30px 0 0;
				display: flex;
				width: 100%;
				justify-content: space-between;
				flex-wrap: wrap;
				.comment-item {
					padding: 8px 10px;
					margin: 0 0 20px;
					width: calc(50% - 10px);
					border-color: #eee;
					border-width: 1px;
					align-items: center;
					position: relative;
					border-style: solid;
					height: auto;
					.istop {
						cursor: pointer;
						box-shadow: none;
						top: 26px;
						background: none;
						position: absolute;
						right: 16px;
						.icon {
							color: #000;
							font-size: 24px;
						}
					}
					.user {
						padding: 10px;
						background: none;
						display: flex;
						width: 100%;
						align-items: center;
						height: auto;
						.el-image {
							border-radius: 100%;
							margin: 0 10px 0 0;
							object-fit: cover;
							width: 40px;
							height: 40px;
						}
						.name {
							color: #333;
							font-weight: 600;
							font-size: 16px;
						}
					}
					.comment-time {
						padding: 0 10px;
						color: #666;
						width: 100%;
						text-align: right;
					}
					.comment-content-box {
						border-radius: 4px;
						padding: 8px;
						box-shadow: none;
						margin: 10px 0px 0px;
						word-wrap: break-word;
						color: #666;
						background: none;
						font-size: 15px;
						line-height: 30px;
						.zancai-box {
							margin: 8px 0 0 0;
							display: none;
							width: 100%;
							justify-content: flex-end;
							align-items: center;
							height: 30px;
							.zan-item {
								display: flex;
								align-items: center;
								.icon {
								font-size: 14px;
								}
								.label {
								display: none;
								font-size: 14px;
								}
								.num {
								font-size: 14px;
								}
							}
							.zan-item.active {
								background: none;
								.icon {
								color: #ff0000;
								font-size: 14px;
								}
								.label {
								color: #ff0000;
								display: none;
								font-size: 14px;
								}
								.num {
								color: #ff0000;
								font-size: 14px;
								}
							}
							.zan-item:hover {
								opacity: 0.8;
								.icon {
								color: #ff000030;
								}
								.label {
								color: #ff000030;
								}
								.num {
								color: #ff000030;
								}
							}
							.cai-item {
								display: flex;
								align-items: center;
								.icon {
								font-size: 14px;
								}
								.label {
								display: none;
								font-size: 14px;
								}
								.num {
								font-size: 14px;
								}
							}
							.cai-item.active {
								background: none;
								.icon {
								color: #ff0000;
								font-size: 14px;
								}
								.label {
								color: #ff0000;
								display: none;
								font-size: 14px;
								}
								.num {
								color: #ff0000;
								font-size: 14px;
								}
							}
							.cai-item:hover {
								opacity: 0.8;
								.icon {
								color: #ff000030;
								}
								.label {
								color: #ff000030;
								}
								.num {
								color: #ff000030;
								}
							}
						}
						.comment-btn {
							margin: 8px 0 0 0;
							display: flex;
							width: 100%;
							justify-content: flex-end;
							align-items: center;
							height: 40px;
							.delBtn {
								border: 0;
								cursor: pointer;
								border-radius: 2px;
								padding: 0 20px;
								margin: 0 10px;
								outline: none;
								color: #f00;
								background: #e61f4d20;
								width: auto;
								font-size: 14px;
								line-height: 34px;
								height: 34px;
							}
						}
					}
				}
			}
			.el-rate {
				padding: 0;
				width: 100%;
				line-height: 40px;
				height: auto;
				::v-deep .el-rate__item {
					cursor: pointer;
					display: inline-block;
					vertical-align: middle;
					position: relative;
				}
				
				::v-deep .el-rate__item .el-rate__icon {
					margin: 0 3px;
					display: block;
					font-size: 18px;
					position: relative;
					transition: .3s;
				}
			}
		}
	}
</style>
