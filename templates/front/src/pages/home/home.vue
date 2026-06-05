<template>
	<div class="home-preview">




		<!-- 新闻资讯 -->
		<div id="animate_newsnews" class="news animate__animated">
			<div class="news_title_box">
				<span class="news_title">系统公告</span>
				<span class="news_subhead">{{'news'.toUpperCase()}}</span>
			</div>
			<div v-if="newsList.length" class="list list20 index-pv1">
				<div v-for="(item,index) in newsList" :key="index"  @click="toDetail('newsDetail', item)" class="list-item animation-box">
					<div class="img-box">
						<img :src="baseUrl + (item.picture?item.picture.split(',')[0]:'')" class="image">
					</div>
					<div class="infoBox">
						<div class="infoBox-left">
							<div class="name">{{item.title}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{item.addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{item.name}}</span>
							</div>
						</div>
						<div class="desc">{{item.introduction}}</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('news')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-jinru"></i>
			</div>
		</div>
		<!-- 新闻资讯 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendautohome" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">新能源资讯推荐</span>
				<span class="recommend_subhead">{{'autohome'.toUpperCase()}} RECOMMEND</span>
			</div>
			<!-- 样式一 -->
			<div class="list list1 index-pv1">
				<div v-for="(item,index) in autohomeRecommend" :key="index" @click="toDetail('autohomeDetail', item)" class="list-item animation-box">
					<img v-if="preHttp(item.imgurl)&&preHttp2(item.imgurl)" :src="item.imgurl" alt="" />
					<img v-else-if="preHttp(item.imgurl)" :src="item.imgurl.split(',')[0]" alt="" />
					<img v-else :src="baseUrl + (item.imgurl?item.imgurl.split(',')[0]:'')" alt="" />
					<div class="name line1">{{item.title}}</div>
				
					<div class="time_item">
						<span class="icon iconfont icon-shijian21"></span>
						<span class="label">发布时间：</span>
						<span class="text">{{item.addtime.split(' ')[0]}}</span>
					</div>
					<div class="like_item">
						<span class="icon iconfont icon-zan10"></span>
						<span class="label">点赞数：</span>
						<span class="text">{{item.thumbsupnum}}</span>
					</div>
					<div class="collect_item">
						<span class="icon iconfont icon-shoucang10"></span>
						<span class="label">收藏量：</span>
						<span class="text">{{item.storeupnum}}</span>
					</div>
					<div class="view_item">
						<span class="icon iconfont icon-chakan2"></span>
						<span class="label">点击量：</span>
						<span class="text">{{item.clicknum}}</span>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('autohome')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-jinru"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendxingyezixun" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">行业资讯推荐</span>
				<span class="recommend_subhead">{{'xingyezixun'.toUpperCase()}} RECOMMEND</span>
			</div>
			<!-- 样式一 -->
			<div class="list list1 index-pv1">
				<div v-for="(item,index) in xingyezixunRecommend" :key="index" @click="toDetail('xingyezixunDetail', item)" class="list-item animation-box">
					<img v-if="preHttp(item.fengmian)&&preHttp2(item.fengmian)" :src="item.fengmian" alt="" />
					<img v-else-if="preHttp(item.fengmian)" :src="item.fengmian.split(',')[0]" alt="" />
					<img v-else :src="baseUrl + (item.fengmian?item.fengmian.split(',')[0]:'')" alt="" />
					<div class="name line1">{{item.zixunbiaoti}}</div>
				
					<div class="time_item">
						<span class="icon iconfont icon-shijian21"></span>
						<span class="label">发布时间：</span>
						<span class="text">{{item.addtime.split(' ')[0]}}</span>
					</div>
					<div class="like_item">
						<span class="icon iconfont icon-zan10"></span>
						<span class="label">点赞数：</span>
						<span class="text">{{item.thumbsupnum}}</span>
					</div>
					<div class="collect_item">
						<span class="icon iconfont icon-shoucang10"></span>
						<span class="label">收藏量：</span>
						<span class="text">{{item.storeupnum}}</span>
					</div>
					<div class="view_item">
						<span class="icon iconfont icon-chakan2"></span>
						<span class="label">点击量：</span>
						<span class="text">{{item.clicknum}}</span>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('xingyezixun')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-jinru"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
		<!-- 特价商品 -->
		<div id="animate_listautohome" class="lists animate__animated">
			<div class="list_title_box">
				<span class="list_title">新能源资讯排行榜</span>
				<span class="list_subhead">{{'autohome'.toUpperCase()}} SHOW</span>
			</div>
			<!-- 样式二 -->
			<div class="list list2 index-pv1">
				<div v-for="(item,index) in autohomeList" class="list-item animation-box" :key="index" @click="toDetail('autohomeDetail', item)">
					<img v-if="preHttp(item.imgurl)&&preHttp2(item.imgurl)" :src="item.imgurl" alt="" />
					<img v-else-if="preHttp(item.imgurl)" :src="item.imgurl.split(',')[0]" alt="" />
					<img v-else :src="baseUrl + (item.imgurl?item.imgurl.split(',')[0]:'')" alt="" />
					<div class="item-info">
						<div class="name line1">{{item.title}}</div>
						<div class="time_item">
							<span class="icon iconfont icon-shijian21"></span>
							<span class="label">发布时间：</span>
							<span class="text">{{item.addtime.split(' ')[0]}}</span>
						</div>
						<div class="like_item">
							<span class="icon iconfont icon-zan10"></span>
							<span class="label">点赞数：</span>
							<span class="text">{{item.thumbsupnum}}</span>
						</div>
						<div class="collect_item">
							<span class="icon iconfont icon-shoucang10"></span>
							<span class="label">收藏量：</span>
							<span class="text">{{item.storeupnum}}</span>
						</div>
						<div class="view_item">
							<span class="icon iconfont icon-chakan2"></span>
							<span class="label">点击量：</span>
							<span class="text">{{item.clicknum}}</span>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('autohome')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-jinru"></i>
			</div>
	

		</div>
		<!-- 特价商品 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				newsList: [],
				autohomeRecommend: [],
				xingyezixunRecommend: [],

				autohomeList: [],




			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getNewsList();
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		computed: {
			username() {
				return localStorage.getItem('username')
			}
		},
		//方法集合
		methods: {
			swiperChanges() {
				setTimeout(()=>{
				},750)
			},


			handleScroll() {
				let arr = [
					{id:'about',css:'animate__'},
					{id:'system',css:'animate__'},
					{id:'animate_recommendautohome',css:'animate__'},
					{id:'animate_listautohome',css:'animate__'},
					{id:'animate_recommendxingyezixun',css:'animate__'},
					{id:'animate_newsnews',css:'animate__'},
				]
			
				for (let i in arr) {
					let doc = document.getElementById(arr[i].id)
					if (doc) {
						let top = doc.offsetTop
						let win_top = window.innerHeight + window.pageYOffset
						// console.log(top,win_top)
						if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
							// console.log(doc)
							doc.classList.add(arr[i].css)
						}
					}
				}
			},
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getNewsList() {
				let data = {
					page: 1,
					limit: 3,
					sort: 'addtime',
					order: 'desc'
				}
				this.$http.get('news/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
					
					}
				});
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "autohome/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "autohome/autoSort2";
				}
				data = {
					page: 1,
					limit: 8,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.autohomeRecommend = res.data.data.list;
					}
				});
				autoSortUrl = "xingyezixun/autoSort";
				data = {
					page: 1,
					limit: 8,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.xingyezixunRecommend = res.data.data.list;
					}
				});
			
				data = {
					page: 1,
					limit: 6,
				}
				data['sort'] = 'liulan'
				data['order']= 'desc'

				this.$http.get('autohome/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.autohomeList = res.data.data.list;
					}
				});
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id, storeupType: 1}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		margin: 0 auto;
		display: flex;
		width: 100%;
		justify-content: space-between;
		flex-wrap: wrap;
		.news {
			padding: 20px 7% 20px;
			margin: 0 auto;
			background: #fff;
			width: 100%;
			position: relative;
			order: 5;
			.news_title_box {
				margin: 0 0 20px 0;
				background: none;
				display: flex;
				width: 100%;
				line-height: 54px;
				flex-wrap: wrap;
				.news_title {
					padding: 0;
					color: #333;
					background: none;
					font-weight: 600;
					display: block;
					width: 100%;
					font-size: 35px;
					line-height: 1.5;
					text-align: center;
					order: 2;
				}
				.news_subhead {
					margin: 0;
					color: #05441a;
					width: 100%;
					font-size: 16px;
					line-height: 1.5;
					text-align: center;
				}
			}
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1.1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list20 {
				padding: 0;
				margin: 0 0 0 -10px;
				color: #666;
				background: none;
				display: flex;
				width: calc(100% + 20px);
				font-size: 14px;
				flex-wrap: wrap;
				height: auto;
				.list-item {
					margin: 10px 10px 20px 10px;
					background: none;
					display: flex;
					width: calc(33.33% - 20px);
					position: relative;
					flex-wrap: wrap;
					height: auto;
					.img-box {
						border-radius: 20px 20px 5px 5px;
						padding: 0;
						overflow: hidden;
						width: 100%;
						height: auto;
						img {
							padding: 0;
							object-fit: cover;
							display: block;
							width: 100%;
							height: 320px;
						}
					}
					.infoBox {
						width: 100%;
						.infoBox-left {
							padding: 0;
							color: #666;
							align-content: center;
							display: flex;
							width: 100%;
							font-size: 14px;
							justify-content: center;
							align-items: center;
							flex-wrap: wrap;
							.name {
								padding: 0;
								overflow: hidden;
								color: #333;
								white-space: nowrap;
								font-weight: 500;
								width: 100%;
								font-size: 18px;
								line-height: 50px;
								text-overflow: ellipsis;
								text-align: center;
							}
							.time_item {
								padding: 0;
								width: 100%;
								text-align: center;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 28px;
								}
							}
							.like_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 28px;
								}
							}
							.collect_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 28px;
								}
							}
							.view_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 28px;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 28px;
								}
							}
						}
						.desc {
							color: #666;
							display: none;
							font-size: 12px;
							line-height: 1.5;
						}
					}
					
				}
				.list-item:hover {
					cursor: pointer;
					background: none;
					.infoBox {
						.infoBox-left {
							.name {
							}
							.time_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
							.publisher_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
							.like_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
							.collect_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
							.view_item {
								.icon {
								}
								.label {
								}
								.text {
								}
							}
						}
						.desc {
							color: #fff;
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #ddd;
				cursor: pointer;
				padding: 0 10px 0 20px;
				margin: 90px auto 0;
				z-index: 3;
				display: flex;
				line-height: 40px;
				right: 7%;
				border-radius: 30px;
				top: 0;
				background: #05441a10;
				width: auto;
				justify-content: center;
				position: absolute;
				.text {
					margin: 0 5px 0 0;
					color: #05441a;
					font-size: 16px;
				}
				.icon {
					color: #05441a;
					background: none;
					display: inline-block;
					width: 23px;
					font-size: 16px;
					height: 7px;
				}
			}
		}
		.recommend {
			padding: 60px 7% 60px;
			margin: 0 auto 0;
			background: #fff;
			width: 100%;
			position: relative;
			order: 1;
			.recommend_title_box {
				margin: 0 0 20px 0;
				background: none;
				display: flex;
				width: 100%;
				line-height: 54px;
				flex-wrap: wrap;
				.recommend_title {
					padding: 0;
					color: #333;
					background: none;
					font-weight: 600;
					display: block;
					width: 80%;
					font-size: 35px;
					line-height: 1.5;
					text-align: left;
					order: 2;
				}
				.recommend_subhead {
					margin: 0;
					color: #05441a;
					width: 80%;
					font-size: 16px;
					line-height: 1.5;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, -4px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list1 {
				padding: 0;
				margin: 0 0 0 -10px;
				color: #666;
				background: none;
				width: calc(100% + 20px);
				font-size: 12px;
				height: auto;
				.list-item {
					cursor: pointer;
					filter: drop-shadow(0 0 9px rgba(2,2,2,0.1));
					border-radius: 20px;
					padding: 20px ;
					margin: 0 15px 20px;
					background: #fff;
					display: inline-flex;
					width: calc(25% - 30px);
					position: relative;
					flex-wrap: wrap;
					height: auto;
					img {
						border-radius: 6px;
						margin: 0 0 5px 0;
						object-fit: cover;
						display: block;
						width: 100%;
						height: 275px;
					}
					.name {
						padding: 0;
						overflow: hidden;
						color: #333;
						white-space: nowrap;
						width: 100%;
						font-size: 16px;
						line-height: 1.5;
						text-overflow: ellipsis;
						text-align: center;
					}
					.price {
						padding: 0;
						color: #f00;
						width: 100%;
						font-size: 16px;
						line-height: 1.5;
					}
					.time_item {
						padding: 0 10px 0 0;
						.icon {
							margin: 0 2px 0 0;
							line-height: 1.5;
						}
						.label {
							line-height: 1.5;
						}
						.text {
							line-height: 1.5;
						}
					}
					.publisher_item {
						padding: 0 10px 0 0;
						.icon {
							margin: 0 2px 0 0;
							line-height: 1.5;
						}
						.label {
							line-height: 1.5;
						}
						.text {
							line-height: 1.5;
						}
					}
					.like_item {
						padding: 0 10px 0 0;
						.icon {
							margin: 0 2px 0 0;
							line-height: 1.5;
						}
						.label {
							line-height: 1.5;
						}
						.text {
							line-height: 1.5;
						}
					}
					.collect_item {
						padding: 0 10px 0 0;
						.icon {
							margin: 0 2px 0 0;
							line-height: 1.5;
						}
						.label {
							line-height: 1.5;
						}
						.text {
							line-height: 1.5;
						}
					}
					.view_item {
						padding: 0 10px 0 0;
						.icon {
							margin: 0 2px 0 0;
							line-height: 1.5;
						}
						.label {
							line-height: 1.5;
						}
						.text {
							line-height: 1.5;
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #ddd;
				cursor: pointer;
				padding: 0 10px 0 20px;
				margin: 70px auto 0;
				z-index: 3;
				display: flex;
				line-height: 40px;
				right: 7%;
				border-radius: 30px;
				top: 0;
				background: #05441a10;
				width: auto;
				justify-content: center;
				position: absolute;
				.text {
					margin: 0 5px 0 0;
					color: #05441a;
					font-size: 16px;
				}
				.icon {
					margin: 0 5px 0 0;
					color: #05441a;
					display: inline-block;
					width: auto;
					font-size: 18px;
					height: 7px;
				}
			}
		}
		.lists {
			padding: 80px 7% 80px;
			margin: 0 auto;
			background: #fff;
			width: 100%;
			position: relative;
			order: 3;
			.list_title_box {
				margin: 0 0 20px 0;
				background: none;
				display: flex;
				width: 100%;
				line-height: 54px;
				flex-wrap: wrap;
				.list_title {
					padding: 0;
					color: #333;
					background: none;
					font-weight: 600;
					display: block;
					width: 100%;
					font-size: 35px;
					line-height: 1.5;
					text-align: center;
					order: 2;
				}
				.list_subhead {
					margin: 0;
					color: #05441a;
					width: 100%;
					font-size: 16px;
					line-height: 1.5;
					text-align: center;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list2 {
				padding: 0;
				margin: 30px 0 0 -10px;
				color: #666;
				background: none;
				display: flex;
				width: calc(100% + 20px);
				font-size: 14px;
				justify-content: space-between;
				flex-wrap: wrap;
				height: auto;
				.list-item {
					cursor: pointer;
					filter: drop-shadow(0 0 9px rgba(2,2,2,0.1));
					border-radius: 10px;
					padding: 20px;
					margin: 0 15px 30px;
					background: #fff;
					display: flex;
					width: calc(33.33% - 30px);
					position: relative;
					flex-wrap: wrap;
					height: auto;
					img {
						border-radius: 12px;
						padding: 0;
						background: #fff;
						object-fit: cover;
						display: inline-block;
						width: 100%;
						height: 380px;
					}
					.item-info {
						padding: 5px 0;
						overflow: hidden;
						align-content: center;
						background: none;
						display: flex;
						width: 100%;
						align-items: center;
						flex-wrap: wrap;
						height: auto;
						.name {
							padding: 0;
							overflow: hidden;
							color: #333;
							white-space: nowrap;
							font-weight: 500;
							width: 100%;
							font-size: 16px;
							line-height: 26px;
							text-overflow: ellipsis;
							text-align: center;
						}
						.price {
							padding: 0;
							color: #f00;
							width: 100%;
							font-size: 16px;
							line-height: 2;
						}
						.time_item {
							padding: 0 10px 0 0;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.publisher_item {
							padding: 0 10px 0 0;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.like_item {
							padding: 0 10px 0 0;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.collect_item {
							padding: 0 10px 0 0;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.view_item {
							padding: 0 10px 0 0;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #ddd;
				cursor: pointer;
				padding: 0 10px 0 20px;
				margin: 95px auto 0;
				z-index: 3;
				display: flex;
				line-height: 40px;
				right: 7%;
				border-radius: 30px;
				top: 0;
				background: #05441a10;
				width: auto;
				justify-content: center;
				position: absolute;
				.text {
					margin: 0 5px 0 0;
					color: #05441a;
					font-size: 16px;
				}
				.icon {
					color: #05441a;
					background: none;
					display: inline-block;
					width: 23px;
					font-size: 16px;
					height: 7px;
				}
			}
		}
	}
</style>
