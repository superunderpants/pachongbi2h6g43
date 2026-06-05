<template>
	<div class="main-content" :style='{"padding":"22px 28px"}'>
		<!-- 列表页 -->
		<div v-if="!showFlag" style="width: 100%;">
			<el-form :style='{"width":"100%","padding":"0","margin":"0 0 20px"}' :inline="true" :model="searchForm" class="center-form-pv">
				<el-row :style='{"padding":"30px","borderRadius":"8px 8px 0 0","flexWrap":"wrap","background":"#fff","display":"flex","width":"100%","position":"relative"}'>
					<div :style='{"margin":"0 1% 10px 0","display":"flex"}'>
						<label :style='{"margin":"0 10px 0 0","whiteSpace":"nowrap","color":"#333333","lineHeight":"40px","fontSize":"16px","fontWeight":"bold","height":"40px"}' class="item-label">是否回复</label>
						<el-select v-model="searchForm.isreply" placeholder="请选择">
							<el-option label="已回复" :value="0"></el-option>
							<el-option label="未回复" :value="1"></el-option>
						</el-select>
					</div>
					<div :style='{"margin":"0 1% 10px 0","display":"flex"}'>
						<label :style='{"margin":"0 10px 0 0","whiteSpace":"nowrap","color":"#333333","lineHeight":"40px","fontSize":"16px","fontWeight":"bold","height":"40px"}' class="item-label">是否已读</label>
						<el-select v-model="searchForm.isread" placeholder="请选择">
							<el-option label="已读" :value="1"></el-option>
							<el-option label="未读" :value="0"></el-option>
						</el-select>
					</div>
					<el-button class="search" :style='{"border":"0","cursor":"pointer","padding":"0 12px 0 10px","outline":"none","color":"#10C17C","borderRadius":"24px","background":"#DEF6ED","width":"auto","fontSize":"16px","minWidth":"160px","fontWeight":"bold","height":"41px"}' type="success" @click="search()">
						<span class="icon iconfont icon-fangdajing01" :style='{"margin":"0 0px","fontSize":"16px","color":"#10C17C","height":"40px"}'></span>
						查询
					</el-button>
				</el-row>
			</el-form>
			<div>
				<el-table
					:stripe='false'
					:style='{"padding":"0","borderColor":"#e7e8fc","borderRadius":"0","borderWidth":"0px 0 0 0px","background":"#fff","width":"100%","borderStyle":"solid"}'
					:data="dataList"
					:border='false'
					v-loading="dataListLoading"
					style="width: 100%;"
					>
					<el-table-column
						:resizable='true' :sortable='true'
						prop="allnode"
						header-align="center"
						align="center"
						sortable
						label="用户"
						>
						<template slot-scope="scope">
							<div style="display: flex;align-items: center;">
								<img :src="scope.row.uimage?$base.url + scope.row.uimage.split(',')[0]:require('@/assets/img/avator.png')" style="width: 80px;height: 80px;border-radius: 50%;margin: 0 5px 0 0;" alt="" />
								{{scope.row.uname}}
							</div>
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true' prop="ask" :formatter="askFormat" header-align="center" align="center" sortable label="新消息"></el-table-column>
					<el-table-column
						:resizable='true' :sortable='true'
						prop="allnode"
						header-align="center"
						align="center"
						sortable
						label="是否回复"
						width="150"
						>
						<template slot-scope="scope">
							<el-tag v-if="scope.row.isreply==1" type="success">未回复</el-tag>
							<el-tag v-if="scope.row.isreply==0" type="info">已回复</el-tag>
						</template>
					</el-table-column>
					<el-table-column
						:resizable='true' :sortable='true'
						prop="allnode"
						header-align="center"
						align="center"
						sortable
						label="是否已读"
						width="150"
						>
						<template slot-scope="scope">
							<el-tag v-if="scope.row.isread==1" type="success">已读</el-tag>
							<el-tag v-if="scope.row.isread==0" type="info">未读</el-tag>
						</template>
					</el-table-column>
					<el-table-column
						header-align="center"
						align="center"
						width="150"
						label="操作"
						>
						<template slot-scope="scope">
							<el-button
								type="text"
								:style='{"border":"0px solid #8B2121","cursor":"pointer","padding":"0 10px","margin":"4px","color":"#10C17C","outline":"none","borderRadius":"6px","background":"none","width":"auto","fontSize":"14px","fontWeight":"400","height":"36px","order":"3"}'
								size="small"
								@click="addOrUpdateHandler(scope.row)"
							>回复</el-button>
						</template>
					</el-table-column>
				</el-table>
			
				<el-pagination
					@size-change="sizeChangeHandle"
					@current-change="currentChangeHandle"
					:current-page="pageIndex"
					:page-sizes="[10, 50, 100, 200]"
					:page-size="pageSize"
					:total="totalPage"
					:layout="layouts.join()"
					prev-text="上一页"
					next-text="下一页"
					:hide-on-single-page="false"
					:style='{"padding":"0","margin":"20px 0 0","whiteSpace":"nowrap","color":"#333","display":"flex","width":"100%","fontWeight":"500","justifyContent":"center"}'
				></el-pagination>
			</div>
		</div>
		<!-- 添加/修改页面  将父组件的search方法传递给子组件-->
		<add-or-update v-else :parent="this" ref="addOrUpdate"></add-or-update>
	</div>
</template>
<script>
	import AddOrUpdate from "./chat-add-or-update";
	import { setInterval, clearInterval } from 'timers';
	export default {
		data() {
			return {
				layouts: ["total","prev","pager","next","sizes","jumper"],
				searchForm: {
					isreply:1,
					isread: 0
				},
				dataList: [],
				pageIndex: 1,
				pageSize: 10,
				totalPage: 0,
				dataListLoading: false,
				showFlag: false,
				dataListSelections: [],
				inter: null,
			};
		},
		created() {
			var that = this;
			that.getDataList();
			var inter = setInterval(function(){
				that.getDataList();
			},5000);
			this.inter = inter;
		},
		destroyed(){
			clearInterval(this.inter);
		},
		components: {
			AddOrUpdate
		},
		methods: {
			askFormat(row, column) {
				if (row.ask && row.type==2) {
					return '[图片]'
				} else if(row.ask&&row.type==3) {
					return '[视频]'
				} else if(row.ask&&row.type==4) {
					return '[文件]'
				} else {
					return row.ask
				}
			},
			search() {
				this.pageIndex = 1
				this.getDataList()
			},
			getDataList() {
				let params = {
					page: this.pageIndex,
					limit: this.pageSize,
					sort: 'id',
				}
				params.isreply = this.searchForm.isreply
				params.isread = this.searchForm.isread
				this.dataListLoading = true;
				this.$http({
					url: this.$api.chatpage,
					method: "get",
					params: params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.dataList = data.data.list;
						this.totalPage = data.data.total;
					} else {
						this.dataList = [];
						this.totalPage = 0;
					}
					this.dataListLoading = false;
				});
			},
			// 每页数
			sizeChangeHandle(val) {
				this.pageSize = val;
				this.pageIndex = 1;
				this.getDataList();
			},
			// 当前页
			currentChangeHandle(val) {
				this.pageIndex = val;
				this.getDataList();
			},
			// 回复
			addOrUpdateHandler(row) {
				this.showFlag = true;
				this.$nextTick(() => {
					this.$refs.addOrUpdate.init(row.userid);
				});
			}
		}
	};
</script>
<style lang="scss" scoped>
	.table-content {
		background: transparent;
	}
	
	.center-form-pv .el-select {
				width: 100%;
			}
	
	.center-form-pv .el-select ::v-deep .el-input__inner {
				border: 1px solid #DADFE6;
				border-radius: 4px;
				padding: 0 12px;
				box-shadow: none;
				outline: none;
				color: #212D3F;
				width: 100%;
				font-size: 16px;
				height: 41px;
			}
	
	// table
	.el-table ::v-deep .el-table__header-wrapper thead {
				color: #000000;
				font-weight: 400;
				width: 100%;
			}
	
	.el-table ::v-deep .el-table__header-wrapper thead tr {
				background: none;
			}
	
	.el-table ::v-deep .el-table__header-wrapper thead tr th {
				padding: 12px 0;
				background: none;
				border-color: #545454;
				border-width: 0;
				border-style: dotted;
				text-align: center;
			}
	
	.el-table ::v-deep .el-table__header-wrapper thead tr th .cell {
				padding: 0 0 0 5px;
				word-wrap: normal;
				color: #212D3F;
				white-space: normal;
				font-weight: 400;
				display: flex;
				vertical-align: middle;
				font-size: 15px;
				line-height: 24px;
				text-overflow: ellipsis;
				word-break: break-all;
				width: 100%;
				justify-content: flex-start;
				align-items: center;
				position: relative;
				min-width: 110px;
			}
	
	
	.el-table ::v-deep .el-table__body-wrapper {
				position: relative;
			}
	.el-table ::v-deep .el-table__body-wrapper tbody {
				width: 100%;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr {
				color: #212D3F;
				background: #fff;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td {
				padding: 4px 0;
				color: #000000;
				background: none;
				border-color: #999999;
				border-width: 0 0px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr:hover td {
				padding: 4px 0;
				color: #10C17C;
				background: #DEF6ED;
				border-color: #999999;
				border-width: 0 0px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td {
				padding: 4px 0;
				color: #000000;
				background: none;
				border-color: #999999;
				border-width: 0 0px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .cell {
				padding: 0 0 0 5px;
				overflow: hidden;
				word-break: break-all;
				white-space: normal;
				font-size: inherit;
				line-height: 24px;
				text-overflow: ellipsis;
			}
	
	// pagination
	.main-content .el-pagination ::v-deep .el-pagination__total {
				margin: 0 20px 0 0;
				color: #212D3F;
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				line-height: 40px;
				height: 40px;
			}
	
	.main-content .el-pagination ::v-deep .btn-prev {
				border: 1px solid #333333;
				cursor: not-allowed;
				padding: 0 10px;
				margin: 0 5px;
				color: #333333;
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				border-radius: 8px  8px  8px  8px;
				background: none;
				width: auto;
				height: 40px;
				order: 2;
			}
	
	.main-content .el-pagination ::v-deep .btn-next {
				border: 1px solid #333333;
				cursor: not-allowed;
				padding: 0 10px;
				margin: 0 5px;
				color: #333333;
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				border-radius: 8px  8px  8px  8px;
				background: none;
				width: auto;
				height: 40px;
				order: 5;
			}
	
	.main-content .el-pagination ::v-deep .btn-prev:disabled {
				border: 1px solid #ddd;
				cursor: not-allowed;
				padding: 0 10px;
				margin: 0 5px;
				color: #999;
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				border-radius: 8px  8px  8px  8px;
				background: #eee;
				width: auto;
				height: 40px;
				order: 2;
			}
	
	.main-content .el-pagination ::v-deep .btn-next:disabled {
				border: 1px solid #ddd;
				cursor: not-allowed;
				padding: 0 10px;
				margin: 0 5px;
				color: #999;
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				border-radius: 8px  8px  8px  8px;
				background: #eee;
				width: auto;
				height: 40px;
				order: 2;
			}
	
	.main-content .el-pagination ::v-deep .el-pager {
				padding: 0;
				margin: 0;
				display: inline-block;
				vertical-align: top;
				order: 4;
			}
	
	.main-content .el-pagination ::v-deep .el-pager .number {
				border: 1px solid #000;
				cursor: not-allowed;
				padding: 0;
				margin: 0 5px;
				color: #333333;
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				line-height: 40px;
				border-radius: 8px  8px  8px  8px;
				background: none;
				width: 40px;
				height: 40px;
			}
	
	.main-content .el-pagination ::v-deep .el-pager .number:hover {
				border: 0px solid #333333;
				cursor: not-allowed;
				padding: 0;
				margin: 0 5px;
				color: #fff;
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				line-height: 40px;
				border-radius: 8px  8px  8px  8px;
				box-shadow: inset 0px 3px 6px 1px rgba(0,0,0,0.16);
				background: #10C17C;
				width: 40px;
				height: 40px;
			}
	
	.main-content .el-pagination ::v-deep .el-pager .number.active {
				border: 0px solid #333333;
				cursor: not-allowed;
				padding: 0;
				margin: 0 5px;
				color: #fff;
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				line-height: 40px;
				border-radius: 8px  8px  8px  8px;
				box-shadow: inset 0px 3px 6px 1px rgba(0,0,0,0.16);
				background: #10C17C;
				width: 40px;
				height: 40px;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes {
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				line-height: 40px;
				height: 40px;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes .el-input {
				margin: 0 5px;
				width: 100px;
				position: relative;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes .el-input .el-input__inner {
				border: 1px solid #707070;
				cursor: pointer;
				padding: 0 25px 0 8px;
				color: #333333;
				display: inline-block;
				font-size: 15px;
				line-height: 40px;
				border-radius: 3px;
				outline: 0;
				background: none;
				width: 100%;
				text-align: center;
				height: 40px;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes .el-input span.el-input__suffix {
				top: 0;
				position: absolute;
				right: 0;
				height: 100%;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes .el-input .el-input__suffix .el-select__caret {
				cursor: pointer;
				color: #fff;
				width: 25px;
				font-size: 15px;
				line-height: 28px;
				text-align: center;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__jump {
				margin: 0 0 0 24px;
				color: #333333;
				display: inline-block;
				vertical-align: top;
				font-size: 15px;
				line-height: 40px;
				height: 40px;
				order: 6;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__jump .el-input {
				border-radius: 3px;
				padding: 0 2px;
				margin: 0 2px;
				display: inline-block;
				width: 50px;
				font-size: 15px;
				line-height: 18px;
				position: relative;
				text-align: center;
				height: 28px;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__jump .el-input .el-input__inner {
				border: 1px solid #212D3F;
				cursor: pointer;
				padding: 0 3px;
				color: #333333;
				display: inline-block;
				font-size: 15px;
				line-height: 40px;
				border-radius: 8px;
				outline: 0;
				background: #fff;
				width: 100%;
				text-align: center;
				height: 40px;
			}
</style>
