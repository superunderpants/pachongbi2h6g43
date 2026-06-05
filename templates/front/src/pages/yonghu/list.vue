<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'→'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div v-if="centerType " class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-fanhui01"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="list-preview">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="list-item" >
					<div class="lable">账号：</div>
					<el-input v-model="formSearch.zhanghao" placeholder="账号" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-form-item class="list-item" >
					<div class="lable">姓名：</div>
					<el-input v-model="formSearch.xingming" placeholder="姓名" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<div class="list-btn-box">
					<el-button class="list-search-btn" v-if=" true " type="primary" @click="getList(1, curFenlei)">
						<span class="icon iconfont icon-fangdajing12"></span>
						搜索
					</el-button>
					<el-button class="list-add-btn" v-if="btnAuth('yonghu','新增')" type="primary" @click="add('/index/yonghuAdd')">
						<span class="icon iconfont icon-tianjia7"></span>
						新增
					</el-button>
  
				</div>
			</el-form>
			<div class="list">
				<div class="list5">
					<div v-for="(item,index) in dataList" :key="index" class="list-item" @click.stop="toDetail(item)" >
						<div class="imgbox">
							<img @click.stop="imgPreView(item.touxiang)" v-if="item.touxiang && item.touxiang.substr(0,4)=='http'&&item.touxiang.split(',w').length>1" :src="item.touxiang" class="image" />
							<img @click.stop="imgPreView(item.touxiang.split(',')[0])" v-else-if="item.touxiang && item.touxiang.substr(0,4)=='http'" :src="item.touxiang.split(',')[0]" class="image" />
							<img @click.stop="imgPreView(baseUrl + (item.touxiang?item.touxiang.split(',')[0]:''))" v-else :src="baseUrl + (item.touxiang?item.touxiang.split(',')[0]:'')" class="image" />
						</div>
						<div class="infoBox">
							<div class="name">{{item.xingming}}</div>
							<div class="bottomInfo">
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

	
			<el-pagination
				background
				id="pagination"
				class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				prev-text="<"
				next-text=">"
				:hide-on-single-page="true"
				:layout='["total","prev","pager","next","sizes","jumper"].join()'
				:total="total"
				:page-sizes="pageSizes"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>
		</div>
		<el-dialog title="预览图" :visible.sync="previewVisible" width="50%">
			<img :src="previewImg" alt="" style="width: 100%;">
		</el-dialog>
	</div>
</template>
<script>
	import axios from 'axios';
	export default {
		//数据集合
		data() {
			return {
				layouts: '',
				swiperIndex: -1,
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '用户'
					}
				],
				formSearch: {
					zhanghao: '',
					xingming: '',
				},
				fenlei: [],
				feileiColumn: '',
				dataList: [],
				total: 1,
				pageSize: 12,
				pageSizes: [],
				totalPage: 1,
				curFenlei: '全部',
				isPlain: false,
				indexQueryCondition: '',
				timeRange: [],
				centerType:false,
				previewImg: '',
				previewVisible: false,
				sortType: 'id',
				sortOrder: 'desc',
			}
		},
		async created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0){
				this.centerType = true
			}
			this.baseUrl = this.$config.baseUrl;
			if(this.centerType) {
			}
			await this.getFenlei();
			let fenlei = '全部'
			if(this.$route.query.homeFenlei){
				fenlei = this.$route.query.homeFenlei
			}
			this.getList(1, fenlei);
		},
		watch:{
			$route(newValue){
				this.getList(1, newValue.query.homeFenlei);
			}
		},
		computed: {
			role(){
				return localStorage.getItem('frontRole');
			},
			username() {
				return localStorage.getItem('username')
			}
		},
		//方法集合
		methods: {
			queryChange(arr){
				for(let x in arr) {
					if(arr[x] == this.role) {
						return true
					}
				}
				return false
			},
			add(path) {
				let query = {}
				if(this.centerType){
					query.centerType = 1
				}
				this.$router.push({path: path,query:query});
			},
			async getFenlei() {
			},
			getList(page, fenlei, ref = '') {
				let params = {
					page,
					limit: this.pageSize,
				};
				let searchWhere = {};
				if (this.formSearch.zhanghao != ''&&this.formSearch.zhanghao != undefined) searchWhere.zhanghao = '%' + this.formSearch.zhanghao + '%';
				if (this.formSearch.xingming != ''&&this.formSearch.xingming != undefined) searchWhere.xingming = '%' + this.formSearch.xingming + '%';
				let user = JSON.parse(localStorage.getItem('sessionForm'))
				if (this.sortType) searchWhere.sort = this.sortType
				if (this.sortOrder) searchWhere.order = this.sortOrder
				this.$http.get(`yonghu/${this.centerType?'page':'list'}`, {params: Object.assign(params, searchWhere)}).then(async res => {
					if (res.data.code == 0) {
						this.dataList = res.data.data.list;
						this.total = Number(res.data.data.total);
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			curChange(page) {
				this.getList(page);
			},
			prevClick(page) {
				this.getList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getList(1);
			},
			nextClick(page) {
				this.getList(page);
			},
			imgPreView(url){
				this.previewImg = url
				this.previewVisible = true
			},
			toDetail(item) {
				let params = {
					id: item.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/yonghuDetail', query: params});
			},
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			backClick() {
				this.$router.push({path: '/index/center'});
			},

			chapterClick (row){
				let params = {
					refid: row.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/chapteryonghu', query: params});
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.list-preview {
		padding: 0 7%;
		margin: 0 auto;
		align-content: flex-start;
		background: #f9f9f9;
		display: flex;
		width: 100%;
		align-items: flex-start;
		position: relative;
		flex-wrap: wrap;
		.list-form-pv {
			padding: 0 0 20px;
			margin: 0px auto;
			background: none;
			display: flex;
			width: 100%;
			align-items: center;
			flex-wrap: wrap;
			height: auto;
			.list-item {
				margin: 0 5px 0 0;
				::v-deep .el-form-item__content {
					display: flex;
				}
				.lable {
					padding: 0;
					color: #333;
					white-space: nowrap;
					display: inline-block;
					width: auto;
					line-height: 42px;
				}
				.el-input {
					width: 100%;
				}
				.datetimerange {
					border: 1px solid #ddd;
					border-radius: 2px;
					padding: 3px 0px;
					outline: none;
					background: #fff;
					width: auto;
					justify-content: center;
				}
				.el-input ::v-deep .el-input__inner {
					border: 1px solid #ddd;
					border-radius: 2px;
					padding: 0 10px;
					margin: 0;
					outline: none;
					color: #333;
					width: 140px;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
				.el-select {
					width: 100%;
				}
				.el-select ::v-deep .el-input__inner {
					border: 1px solid #ddd;
					border-radius: 2px;
					padding: 0 10px;
					margin: 0;
					outline: none;
					color: #333;
					width: 140px;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
				.el-date-editor {
					width: 100%;
				}
				.el-date-editor ::v-deep .el-input__inner {
					border: 1px solid #ddd;
					border-radius: 2px;
					padding: 0 30px;
					margin: 0;
					outline: none;
					color: #333;
					width: 140px;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
			}
			.list-btn-box {
				display: flex;
			}
			.list-search-btn {
				cursor: pointer;
				border: 0;
				border-radius: 4px;
				padding: 0px 10px;
				margin: 0 10px 0 0;
				outline: none;
				color: #fff;
				background: #05441a;
				width: auto;
				font-size: 15px;
				line-height: 42px;
				height: 42px;
				.icon {
					margin: 0 3px 0 0;
					color: #fff;
					font-size: 16px;
				}
			}
			.list-add-btn {
				cursor: pointer;
				border: 0;
				border-radius: 4px;
				padding: 0px 10px;
				margin: 0 10px 0 0;
				outline: none;
				color: #fff;
				background: #35c34c;
				width: auto;
				font-size: 15px;
				line-height: 42px;
				height: 42px;
				.icon {
					margin: 0 3px 0 0;
					color: #fff;
					font-size: 16px;
				}
			}
		}
		.list {
			margin: 20px 0 0;
			background: none;
			flex: 1;
			width: calc(100% - 360px);
			order: 3;
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
				
			.index-pv1 .animation-box:hover {
				transform: rotate(0) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
				
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list5 {
				margin: 0px auto 20px -10px;
				display: flex;
				width: calc(100% + 20px);
				flex-wrap: wrap;
				.list-item {
					border: 0px solid #eee;
					border-radius: 0px;
					padding: 0px;
					margin: 0 10px 20px;
					overflow: hidden;
					background: #fff;
					display: block;
					width: calc(33.33% - 20px);
					position: relative;
					.imgbox {
						overflow: hidden;
						width: auto;
						.image {
							filter: saturate(150%);
							padding: 10px;
							transform: rotate(0deg);
							margin: 0;
							background: none;
							object-fit: cover;
							display: block;
							width: 100%;
							opacity: 0.9;
							height: 380px;
						}
					}
					.infoBox {
						padding: 0 10px 10px;
						color: #666;
						left: 0px;
						bottom: 0;
						background: none;
						width: 100%;
						font-size: 14px;
						position: inherit;
						transition: all 0.5s;
						.name {
							overflow: hidden;
							color: #333;
							white-space: nowrap;
							width: 100%;
							font-size: 16px;
							text-overflow: ellipsis;
						}
						.price {
							color: #ff0303;
							font-size: 14px;
							.price_text {
								color: #ff0303;
								font-size: 18px;
							}
						}
						.bottomInfo {
							display: flex;
							flex-wrap: wrap;
							.time_item {
								padding: 0;
								margin: 0 10px 0 0;
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
								padding: 0;
								margin: 0 10px 0 0;
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
								padding: 0;
								margin: 0 10px 0 0;
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
								padding: 0;
								margin: 0 10px 0 0;
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
								padding: 0;
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
				.list-item:hover {
					cursor: pointer;
					background: #05441a;
					.imgbox {
						.image {
							transform: scale(1);
							ilter: saturate(100%);
							opacity: 1;
							transition: all 200ms linear;
						}
					}
					.infoBox {
						bottom: 0px;
						font-size: 14px;
						.name {
							color: #fff;
						}
						.price {
							.price_text {
							}
						}
						.bottomInfo {
							display: flex;
							flex-wrap: wrap;
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
								}
								.text {
									color: #fff;
								}
							}
						}
					}
				}
			}
		}
	}
</style>
