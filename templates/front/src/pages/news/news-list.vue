<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'→'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
	
		<div class="news-preview-pv">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="search-item">
					<el-input v-model="title" placeholder="标题"></el-input>
				</el-form-item>
				<el-button class="search-btn" type="primary" @click="getNewsList(1)">
					<span class="icon iconfont icon-chakan14"></span>
					搜索
				</el-button>
			</el-form>
			
			<!-- category -->
			<div class="list10 index-pv1">
				<div v-for="(item,index) in newsList" :key="index" class="list-item animation-box" @click="toNewsDetail(item)">
					<div class="img">
						<img class="image" :src="baseUrl + (item.picture?item.picture.split(',')[0]:'')" >
					</div>
					<div class="infoBox">
						<div class="infoLeft">
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
		
			<el-pagination
				background
				id="pagination" class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				:page-sizes="pageSizes"
				prev-text="<"
				next-text=">"
				:hide-on-single-page="true"
				:layout='["total","prev","pager","next","sizes","jumper"].join()'
				:total="total"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>
		</div>
	</div>
</template>

<script>
	export default {
		//数据集合
		data() {
			return {
				baseUrl: this.$config.baseUrl,
				breadcrumbItem: [
				  {
					name: '系统公告'
				  }
				],
				newsList: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1,
				layouts: '',
				title: '',
			}
		},
		created() {
			this.getNewsList(1);
		},
		watch:{
			$route(newValue){
				this.getNewsList(1);
			}
		},
		//方法集合
		methods: {
			getNewsList(page) {
				let params = {page, limit: this.pageSize,sort:'addtime',order:'desc'};
				let searchWhere = {};
				if(this.title != '') searchWhere.title = '%' + this.title + '%';
				this.$http.get('news/list', {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			curChange(page) {
				this.getNewsList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getNewsList(1);
			},
			prevClick(page) {
				this.getNewsList(page);
			},
			nextClick(page) {
				this.getNewsList(page);
			},
			toNewsDetail(item) {
				this.$router.push({path: '/index/newsDetail', query: {id: item.id}});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.news-preview-pv {
				padding: 0 7%;
				margin: 0px auto;
				align-content: flex-start;
				background: #f9f9f9;
				display: flex;
				width: 100%;
				align-items: flex-start;
				position: relative;
				flex-wrap: wrap;
				.list-form-pv {
						padding: 0px;
						margin: 0 0 20px;
						background: none;
						display: flex;
						width: 100%;
						justify-content: center;
						align-items: center;
						flex-wrap: wrap;
						height: auto;
						.search-item {
								margin: 0 10px 0 0;
								.el-input {
										width: 100%;
									}
				.el-input ::v-deep .el-input__inner {
										border: 1px solid #ddd;
										border-radius: 4px;
										padding: 0 10px;
										margin: 0;
										outline: none;
										color: #333;
										background: #fff;
										width: 500px;
										font-size: 16px;
										line-height: 42px;
										height: 42px;
									}
			}
			.search-btn {
								cursor: pointer;
								border: 0px solid #4789d550;
								border-radius: 4px;
								padding: 0px 15px;
								margin: 0 10px 0 0;
								outline: none;
								color: #fff;
								background: #05441a;
								width: auto;
								font-size: 16px;
								line-height: 42px;
								height: 42px;
								.icon {
										margin: 0 3px 0 0;
										color: #fff;
										font-size: 16px;
									}
			}
		}
		.category-list {
						border: 0px solid #eee;
						padding: 120px 20px 0px;
						margin: 20px 0 0 30px;
						background: url(http://codegen.caihongy.cn/20250815/7bc84b45218d4d31b487bf9bd351cb0a.png) no-repeat center top,#fff;
						display: flex;
						width: 330px;
						justify-content: center;
						flex-wrap: wrap;
						height: auto;
						order: 4;
						.item {
								cursor: pointer;
								border: 0;
								padding: 0 20px;
								margin: 0;
								color: #333;
								font-weight: 600;
								display: flex;
								font-size: 16px;
								line-height: 50px;
								border-radius: 0;
								background: url() no-repeat 90% center;
								width: 100%;
								align-items: center;
							}
			
			.item:hover {
								padding: 0 20px;
								color: #fff;
								background: #05441a;
								font-weight: 600;
								width: 100%;
								font-size: 16px;
								line-height: 50px;
							}
			
			.item.active {
								padding: 0 20px;
								color: #fff;
								background: #05441a;
								font-weight: 600;
								width: 100%;
								font-size: 16px;
								line-height: 50px;
							}
		}
		.list10 {
						padding: 0;
						margin: 0 0 0 -10px;
						background: none;
						flex: 1;
						display: flex;
						width: calc(100% - 360px);
						flex-wrap: wrap;
						height: auto;
						order: 3;
						.list-item {
								cursor: pointer;
								padding: 10px;
								margin: 20px 10px 0;
								background: #fff;
								display: flex;
								width: calc(33.33% - 20px);
								position: relative;
								flex-wrap: wrap;
								height: auto;
								.img {
										overflow: hidden;
										width: 100%;
										height: auto;
										img {
												object-fit: cover;
												display: block;
												width: 100%;
												height: 300px;
											}
				}
				.infoBox {
										padding: 0;
										overflow: hidden;
										display: flex;
										width: 100%;
										height: auto;
										.infoLeft {
												padding: 0 10px 0 0;
												color: #666;
												align-content: center;
												display: flex;
												width: 100%;
												font-size: 14px;
												align-items: center;
												flex-wrap: wrap;
												.name {
														padding: 0;
														overflow: hidden;
														color: #333;
														white-space: nowrap;
														font-weight: 600;
														width: 100%;
														font-size: 15px;
														line-height: 36px;
														text-overflow: ellipsis;
													}
						.time_item {
														padding: 0 15px 0 0;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
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
														padding: 0 15px 0 0;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
															}
							.label {
																display: none;
																line-height: 1.5;
															}
							.text {
																line-height: 28px;
															}
						}
						.like_item {
														padding: 0 15px 0 0;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
															}
							.label {
																display: none;
																line-height: 1.5;
															}
							.text {
																line-height: 28px;
															}
						}
						.collect_item {
														padding: 0 15px 0 0;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
															}
							.label {
																display: none;
																line-height: 1.5;
															}
							.text {
																line-height: 28px;
															}
						}
						.view_item {
														padding: 0 15px 0 0;
														.icon {
																margin: 0 2px 0 0;
																line-height: 28px;
															}
							.label {
																display: none;
																line-height: 1.5;
															}
							.text {
																line-height: 28px;
															}
						}
					}
					.desc {
												color: #666;
												flex: 1;
												display: none;
												font-size: 12px;
												line-height: 1.5;
											}
				}
			}
			.list-item:hover {
								background: #05441a;
								.infoBox {
					.infoLeft {
						.name {
														color: #fff;
													}
						.time_item {
							.icon {
																color: #fff;
															}
							.label {
																color: #fff;
															}
							.text {
																color: #fff;
															}
						}
						.publisher_item {
							.icon {
																color: #fff;
															}
							.label {
																color: #fff;
															}
							.text {
																color: #fff;
															}
						}
						.like_item {
							.icon {
																color: #fff;
															}
							.label {
																color: #fff;
															}
							.text {
																color: #fff;
															}
						}
						.collect_item {
							.icon {
																color: #fff;
															}
							.label {
																color: #fff;
															}
							.text {
																color: #fff;
															}
						}
						.view_item {
							.icon {
																color: #fff;
															}
							.label {
																color: #fff;
															}
							.text {
																color: #fff;
															}
						}
					}
					.desc {
												color: #fff;
											}
				}
			}
		}
	}
	
	.index-pv1 .animation-box {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		z-index: initial;
	}
	
	.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 6px, 0px);
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
</style>
