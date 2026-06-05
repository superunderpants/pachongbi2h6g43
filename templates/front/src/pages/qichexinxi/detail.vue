<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'→'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/qichexinxi?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
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
							{{detail.chepinpai}} - {{detail.chexinghao}}
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
						<div class="lable">汽车品牌</div>
						<div class="text">{{detail.chepinpai}}</div>
					</div>
					<div class="item">
						<div class="lable">车型型号</div>
						<div class="text">{{detail.chexinghao}}</div>
					</div>
					<div class="item">
						<div class="lable">价格区间</div>
						<div class="text">{{detail.jiage}}</div>
					</div>
					<div class="item">
						<div class="lable">月销量</div>
						<div class="text">{{detail.xiaoliang}}</div>
					</div>
					<div class="item">
						<div class="lable">事故率(%)</div>
						<div class="text">{{detail.shigulv}}</div>
					</div>
					<div class="item">
						<div class="lable">续航里程(km)</div>
						<div class="text">{{detail.xuhang}}</div>
					</div>
					<div class="item">
						<div class="lable">电池类型</div>
						<div class="text">{{detail.dianchileixing}}</div>
					</div>
					<div class="item">
						<div class="lable">车身类型</div>
						<div class="text">{{detail.cheshenleixing}}</div>
					</div>
					<div class="item">
						<div class="lable">上市时间</div>
						<div class="text">{{detail.shangshishijian}}</div>
					</div>
					<div class="item">
						<div class="lable">简介</div>
						<div class="text">{{detail.jianjie}}</div>
					</div>
					<div class="item">
						<div class="lable">详细参数</div>
						<div class="text">{{detail.canshu}}</div>
					</div>
					<div class="item">
						<div class="lable">点击次数</div>
						<div class="text">{{detail.clicknum}}</div>
					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('qichexinxi','修改')" @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('qichexinxi','删除')" @click="delClick">删除</el-button>
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
		</div>
	</div>
</template>

<script>
	import axios from 'axios'
	import Swiper from "swiper";
	export default {
		data() {
			return {
				tablename: 'qichexinxi',
				baseUrl: '',
				breadcrumbItem: [
					{ name: '汽车信息' }
				],
				title: '',
				detailBanner: [],
				userid: Number(localStorage.getItem('frontUserid')),
				id: 0,
				detail: {},
				storeupParams: {
					name: '',
					picture: '',
					refid: 0,
					tablename: 'qichexinxi',
					userid: Number(localStorage.getItem('frontUserid'))
				},
				isStoreup: false,
				storeupInfo: {},
				isCrazilynum: false,
				isThumbsupnum: false,
				thumbsupOrCrazilyInfo: {},
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
				let option21 = {"navigation":{"nextEl":".swiper-button-next","prevEl":".swiper-button-prev"},"loopedSlides":5,"spaceBetween":10}
				option21.thumbs = { swiper: mySwiper22 }
				new Swiper(".mySwiper21", option21)
			},100)
		},
		methods: {
			init() {
				this.id = this.$route.query.id
				this.baseUrl = this.$config.baseUrl;
				this.$http.get(this.tablename + '/detail/' + this.id, {}).then(async res => {
					if (res.data.code == 0) {
						this.detail = res.data.data;
						this.title = this.detail.chepinpai + ' - ' + this.detail.chexinghao;
						if(this.detail.tupian) {
							this.detailBanner = this.detail.tupian.split(",w").length>1?[this.detail.tupian]:this.detail.tupian.split(',');
						}
						this.$forceUpdate();
						if(localStorage.getItem('frontToken')){
							this.getStoreupStatus();
							this.getThumbsupOrCrazilyStatus();
						}
					}
				});
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
							this.$http.post('qichexinxi/update', this.detail).then(res => {});
							this.$message({ type: 'success', message: '收藏成功!', duration: 1500 });
						}
					});
				}
				if (type == -1 && this.isStoreup) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '1', refid: this.detail.id, tablename: 'qichexinxi', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isStoreup = true;
							this.storeupInfo = res.data.data.list[0];
							let delIds = [this.storeupInfo.id];
							this.$http.post('storeup/delete', delIds).then(res => {
								if (res.data.code == 0) {
									this.isStoreup = false;
									this.detail.storeupnum--
									this.$http.post('qichexinxi/update', this.detail).then(res => {});
									this.$message({ type: 'success', message: '取消成功!', duration: 1500 });
								}
							});
						}
					});
				}
			},
			getStoreupStatus(){
				if(localStorage.getItem("frontToken")) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '1', refid: this.detail.id, tablename: 'qichexinxi', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
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
						this.$http.post('qichexinxi/update', detail).then(res => {
							this.detail = detail
						});
						this.getThumbsupOrCrazilyStatus();
						this.$message({ type: 'success', message: '操作成功!', duration: 1500 });
					}
				});
			},
			async cancelThumbsupOrCrazily(type) {
				let delIds = [this.thumbsupOrCrazilyInfo.id];
				await this.$http.post('storeup/delete', delIds).then(res => {
					if (res.data.code == 0) {
						let detail = JSON.parse(JSON.stringify(this.detail))
						if (type == 21) detail.thumbsupnum -= 1;
						if (type == 22) detail.crazilynum -= 1;
						this.$http.post('qichexinxi/update', detail).then(res => {
							this.detail = detail
						});
						this.isThumbsupnum = false;
						this.isCrazilynum = false;
						this.$message({ type: 'success', message: '取消成功!', duration: 1500 });
					}
				});
			},
			getThumbsupOrCrazilyStatus() {
				if(localStorage.getItem("frontToken")) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '21', refid: this.detail.id, tablename: 'qichexinxi', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isThumbsupnum = true;
							this.thumbsupOrCrazilyInfo = res.data.data.list[0];
						}
					});
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '22', refid: this.detail.id, tablename: 'qichexinxi', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isCrazilynum = true;
							this.thumbsupOrCrazilyInfo = res.data.data.list[0];
						}
					});
				}
			},
			backClick(){
				if(this.storeupType){
					history.back()
				}else{
					let params = {}
					if(this.centerType){
						params.centerType = 1
					}
					this.$router.push({path: '/index/qichexinxi', query: params});
				}
			},
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			editClick(){
				this.$router.push('/index/qichexinxiAdd?type=edit&&id=' + this.detail.id);
			},
			async delClick(){
				await this.$confirm('是否删除此汽车信息？').then(_ => {
					this.$http.post('qichexinxi/delete', [this.detail.id]).then(async res => {
						if (res.data.code == 0) {
							this.$http.get('storeup/list',{params:{
								page: 1, limit: 100, refid: this.detail.id, tablename: 'qichexinxi',
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
										type: 'success', message: '删除成功!', duration: 1500,
										onClose: () => { history.back() }
									});
								}
							})
						}
					});
				}).catch(_ => {});
			},
		},
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
						.icon { color: #666; font-size: 16px; }
						.text { color: #666; font-size: 16px; }
					}
					.colectBtnActive {
						background: #f60; border-color: #f60;
						.icon { color: #fff; font-size: 16px; }
						.text { color: #fff; font-size: 16px; }
					}
					.colectBtn:hover { background: #f60; border-color: #f60; .icon { color: #fff; } .text { color: #fff; } }
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
					.text {
						padding: 0 10px;
						color: #666;
						word-break: break-all;
						flex: 1;
						font-size: 14px;
						line-height: 24px;
						height: auto;
					}
				}
				.btn_box {
					padding: 10px 0;
					display: flex;
					flex-wrap: wrap;
				}
				.editBtn {
					border: 0; cursor: pointer; border-radius: 0px; padding: 0 10px;
					margin: 0 5px 0 0; outline: none; color: #fff;
					background: rgba(64, 158, 255, 1); width: auto; font-size: 14px;
					line-height: 40px; height: 40px;
				}
				.editBtn:hover { opacity: 0.7; }
				.delBtn {
					border: 0; cursor: pointer; border-radius: 0px; padding: 0 10px;
					margin: 0 5px 0 0; outline: none; color: #fff;
					background: rgba(255, 0, 0, 1.0); width: auto; font-size: 14px;
					line-height: 40px; height: 40px;
				}
				.delBtn:hover { opacity: 0.7; }
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
				.swiper-button-prev:after, .swiper-button-next:after { display:none; }
				.swiper-item {
					width: 100%;
					height: auto;
					img { object-fit: cover; width: 100%; height: 400px; }
				}
				.swiper-button-prev { margin: -12px 0 0; top: 50%; width: 24px; height: 24px; .icon { color: #fff; width: 24px; font-size: 24px; height: 24px; } }
				.swiper-button-next { margin: -12px 0 0; top: 50%; width: 24px; height: 24px; .icon { color: #fff; width: 24px; font-size: 24px; height: 24px; } }
			}
			.swiper22 {
				width: 100%;
				height: auto;
				.swiper-button-prev:after, .swiper-button-next:after { display:none; }
				.swiper-item {
					width: 100%;
					opacity: 0.4;
					height: auto;
					img { object-fit: cover; width: 100%; height: 100px; }
				}
				.swiper-slide.swiper-slide-thumb-active div { opacity: 1; }
				.swiper-button-prev { margin: -7px 0 0; top: 50%; width: 14px; height: 14px; .icon { color: #fff; width: 14px; font-size: 14px; height: 14px; } }
				.swiper-button-next { margin: -7px 0 0; top: 50%; width: 14px; height: 14px; .icon { color: #fff; width: 14px; font-size: 14px; height: 14px; } }
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
			.zan, .cai {
				cursor: pointer; border: 0px solid #ddd; border-radius: 4px;
				padding: 10px 20px; background: #fff; display: flex;
				width: auto; justify-content: center; align-items: center;
				.icon { margin: 0 3px; color: #666; font-size: 14px; }
				.text { margin: 0 3px; color: #666; font-size: 16px; }
			}
			.zan { margin: 0 100px 0 0; }
			.zan:hover, .zanActive { background: #05441a; border-color: #05441a; .icon { color: #fff; } .text { color: #fff; } }
			.cai:hover, .caiActive { background: #05441a; border-color: #05441a; .icon { color: #fff; } .text { color: #fff; } }
		}
	}
</style>
