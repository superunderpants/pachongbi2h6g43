
































<template>
	<div class="add-update-preview">
		<el-form
			class="add-update-form"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="200px"
			>
			<el-form-item class="add-item" label="标题" prop="title">
				<el-input v-model="ruleForm.title" 
					placeholder="标题" clearable :readonly="ro.title"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="图片" v-if="type!='cross' || (type=='cross' && !ro.imgurl)" prop="imgurl">
				<file-upload
					tip="点击上传图片"
					action="file/upload"
					:limit="3"
					accept="image/*"
					:multiple="true"
					:disabled="ro.imgurl"
					:fileUrls="ruleForm.imgurl?ruleForm.imgurl:''"
					@change="imgurlUploadChange"
					></file-upload>
			</el-form-item>
			<el-form-item class="add-item" v-else label="图片" prop="imgurl">
				<img v-if="ruleForm.imgurl.substring(0,4)=='http'" class="upload-img" :key="index" :src="ruleForm.imgurl.split(',')[0]">
				<img v-else class="upload-img" :key="index" v-for="(item,index) in ruleForm.imgurl.split(',')" :src="baseUrl+item">
			</el-form-item>
			<el-form-item class="add-item" label="作者" prop="zuozhe">
				<el-input v-model="ruleForm.zuozhe" 
					placeholder="作者" clearable :readonly="ro.zuozhe"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="发布时间" prop="fbtime">
				<el-input v-model="ruleForm.fbtime" 
					placeholder="发布时间" clearable :readonly="ro.fbtime"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="浏览量(万)" prop="liulan">
				<el-input v-model.number="ruleForm.liulan" 
					placeholder="浏览量(万)" clearable :readonly="ro.liulan"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="发布地点" prop="fbaddress">
				<el-input v-model="ruleForm.fbaddress" 
					placeholder="发布地点" clearable :readonly="ro.fbaddress"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="简介" prop="neirong">
				<el-input
					type="textarea"
					:rows="8"
					:disabled="ro.neirong"
					placeholder="简介"
					v-model="ruleForm.neirong">
					</el-input>
			</el-form-item>
			<el-form-item class="add-item" label="详情链接" prop="xqurl">
				<el-input
					type="textarea"
					:rows="8"
					:disabled="ro.xqurl"
					placeholder="详情链接"
					v-model="ruleForm.xqurl">
					</el-input>
			</el-form-item>
			<el-form-item class="add-item" label="全文" prop="alltext">
				<el-input
					type="textarea"
					:rows="8"
					:disabled="ro.alltext"
					placeholder="全文"
					v-model="ruleForm.alltext">
					</el-input>
			</el-form-item>

			<el-form-item class="add-btn-item">
				<el-button class="submitBtn"  type="primary" @click="onSubmit(null)">
					<span class="icon iconfont icon-xiugai17"></span>
					<span class="text">提交</span>
				</el-button>
				<el-button class="closeBtn" @click="back()">
					<span class="icon iconfont icon-shanchu10"></span>
					<span class="text">取消</span>
				</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				id: '',
				baseUrl: '',
				ro:{
					title : false,
					imgurl : false,
					neirong : false,
					xqurl : false,
					zuozhe : false,
					fbtime : false,
					alltext : false,
					liulan : false,
					fbaddress : false,
					thumbsupnum : false,
					crazilynum : false,
					clicktime : false,
					clicknum : false,
					discussnum : false,
					totalscore : false,
					storeupnum : false,
				},
				type: '',
				userTableName: localStorage.getItem('UserTableName'),
				ruleForm: {
					title: '',
					imgurl: '',
					neirong: '',
					xqurl: '',
					zuozhe: '',
					fbtime: '',
					alltext: '',
					liulan: '',
					fbaddress: '',
					thumbsupnum: '',
					crazilynum: '',
					clicktime: '',
					clicknum: '',
					discussnum: '',
					totalscore: '',
					storeupnum: '',
				},

				rules: {
					title: [
					],
					imgurl: [
					],
					neirong: [
					],
					xqurl: [
						{ validator: this.$validate.isURL, trigger: 'blur' },
					],
					zuozhe: [
					],
					fbtime: [
					],
					alltext: [
					],
					liulan: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					fbaddress: [
					],
					thumbsupnum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					crazilynum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					clicktime: [
					],
					clicknum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					discussnum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					totalscore: [
						{ validator: this.$validate.isNumber, trigger: 'blur' },
					],
					storeupnum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
				},
				centerType: false,
			};
		},
		computed: {
			sessionForm() {
				return JSON.parse(localStorage.getItem('sessionForm'))
			},



		},
		components: {
		},
		created() {
			if(this.$route.query.centerType){
				this.centerType = true
			}
			//this.bg();
			let type = this.$route.query.type ? this.$route.query.type : '';
			this.init(type);
			this.baseUrl = this.$config.baseUrl;
		},
		methods: {
			getMakeZero(s) {
				return s < 10 ? '0' + s : s;
			},
			// 下载
			download(file ){
				window.open(`${file}`)
			},
			// 初始化
			init(type) {
				this.type = type;
				if(type=='cross'){
					var obj = JSON.parse(localStorage.getItem('crossObj'));
					for (var o in obj){
						if(o=='title'){
							this.ruleForm.title = obj[o];
							this.ro.title = true;
							continue;
						}
						if(o=='imgurl'){
							this.ruleForm.imgurl = obj[o]?obj[o].split(",")[0]:'';
							this.ro.imgurl = true;
							continue;
						}
						if(o=='neirong'){
							this.ruleForm.neirong = obj[o];
							this.ro.neirong = true;
							continue;
						}
						if(o=='xqurl'){
							this.ruleForm.xqurl = obj[o];
							this.ro.xqurl = true;
							continue;
						}
						if(o=='zuozhe'){
							this.ruleForm.zuozhe = obj[o];
							this.ro.zuozhe = true;
							continue;
						}
						if(o=='fbtime'){
							this.ruleForm.fbtime = obj[o];
							this.ro.fbtime = true;
							continue;
						}
						if(o=='alltext'){
							this.ruleForm.alltext = obj[o];
							this.ro.alltext = true;
							continue;
						}
						if(o=='liulan'){
							this.ruleForm.liulan = obj[o];
							this.ro.liulan = true;
							continue;
						}
						if(o=='fbaddress'){
							this.ruleForm.fbaddress = obj[o];
							this.ro.fbaddress = true;
							continue;
						}
						if(o=='thumbsupnum'){
							this.ruleForm.thumbsupnum = obj[o];
							this.ro.thumbsupnum = true;
							continue;
						}
						if(o=='crazilynum'){
							this.ruleForm.crazilynum = obj[o];
							this.ro.crazilynum = true;
							continue;
						}
						if(o=='clicktime'){
							this.ruleForm.clicktime = obj[o];
							this.ro.clicktime = true;
							continue;
						}
						if(o=='clicknum'){
							this.ruleForm.clicknum = obj[o];
							this.ro.clicknum = true;
							continue;
						}
						if(o=='discussnum'){
							this.ruleForm.discussnum = obj[o];
							this.ro.discussnum = true;
							continue;
						}
						if(o=='totalscore'){
							this.ruleForm.totalscore = obj[o];
							this.ro.totalscore = true;
							continue;
						}
						if(o=='storeupnum'){
							this.ruleForm.storeupnum = obj[o];
							this.ro.storeupnum = true;
							continue;
						}
					}
				}else if(type=='edit'){
					this.info()
				}

				if (localStorage.getItem('raffleType') && localStorage.getItem('raffleType') != null) {
					localStorage.removeItem('raffleType')
					setTimeout(() => {
						this.onSubmit(null)
					}, 300)
				}
			},

			// 多级联动参数
			// 多级联动参数
			async info() {
				await this.$http.get(`autohome/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.ruleForm = res.data.data;
					}
				});
			},
			// 提交
			async onSubmit(subMitType=null) {
				await this.$refs["ruleForm"].validate(async valid => {
					if(valid) {
						if(!this.ruleForm.id) {
							delete this.ruleForm.userid
						}
						if(this.type=='cross'){
							var statusColumnName = localStorage.getItem('statusColumnName');
							var statusColumnValue = localStorage.getItem('statusColumnValue');
							if(statusColumnName && statusColumnName!='') {
								var obj = JSON.parse(localStorage.getItem('crossObj'));
								if(!statusColumnName.startsWith("[")) {
									for (var o in obj){
										if(o==statusColumnName){
											obj[o] = statusColumnValue;
										}
									}
									var table = localStorage.getItem('crossTable');
									await this.$http.post(table+'/update', obj)
								}
							}
						}

						await this.$http.post(`autohome/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(async res => {
							if (res.data.code == 0) {
								await this.$message({
									message: '操作成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.$router.go(-1);
										
									}
								});
							} else {
								this.$message({
									message: res.data.msg,
									type: 'error',
									duration: 1500
								});
							}
						});
					}
				});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.$router.go(-1);
			},
			imgurlUploadChange(fileUrls) {
				this.ruleForm.imgurl = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
			},
		}
	};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.add-update-preview {
		padding: 20px 7% 40px;
		margin: 0px auto;
		background: #f9f9f9;
		width: 100%;
		position: relative;
		.add-update-form {
			border-radius: 0px;
			padding: 30px 0 20px;
			background: #fff;
			width: 100%;
			position: relative;
			.add-item.el-form-item {
				padding: 0px;
				margin: 0 0 26px;
				background: none;
				display: inline-block;
				width: calc(50% - 20px);
				float: left;
				::v-deep .el-form-item__label {
					padding: 0 10px 0 0;
					color: #333;
					white-space: nowrap;
					font-weight: 500;
					width: 200px;
					font-size: 16px;
					line-height: 40px;
					text-align: right;
				}
				::v-deep .el-form-item__content {
					margin-left: 200px;
				}
				.el-input {
					width: 100%;
				}
				.el-input ::v-deep .el-input__inner {
					border: 0px solid #ddd;
					border-radius: 0px;
					padding: 0 12px;
					box-shadow: none;
					outline: none;
					color: #666;
					width: 100%;
					font-size: 16px;
					border-width: 0 0 1px;
					height: 40px;
				}
				.el-input ::v-deep .el-input__inner[readonly="readonly"] {
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 0 12px;
					box-shadow: none;
					outline: none;
					color: rgba(85, 85, 127, 1.0);
					width: 100%;
					font-size: 16px;
					height: 40px;
				}
				.el-input-number ::v-deep .el-input__inner {
					text-align: left;
					border: 0px solid #ddd;
					border-radius: 0px;
					padding: 0 12px;
					box-shadow: none;
					outline: none;
					color: #666;
					width: 100%;
					font-size: 16px;
					border-width: 0 0 1px;
					height: 40px;
				}
				.el-input-number ::v-deep .is-disabled .el-input__inner {
					text-align: left;
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 0 12px;
					box-shadow: none;
					outline: none;
					color: rgba(85, 85, 127, 1.0);
					width: 100%;
					font-size: 16px;
					height: 40px;
				}
				.el-input-number ::v-deep .el-input-number__decrease {
					display: none;
				}
				.el-input-number ::v-deep .el-input-number__increase {
					display: none;
				}
				.el-select {
					width: 100%;
				}
				.el-select ::v-deep .el-input__inner {
					border: 0px solid #ddd;
					border-radius: 0px;
					padding: 0 10px;
					box-shadow: none;
					outline: none;
					color: rgba(64, 158, 255, 1);
					width: 100%;
					font-size: 14px;
					border-width: 0 0 1px;
					height: 40px;
				}
				.el-select ::v-deep .is-disabled .el-input__inner {
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 0 10px;
					box-shadow: none;
					outline: none;
					color: rgba(85, 85, 127, 1.0);
					background: #eee;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-date-editor {
					width: 100%;
				}
				.el-date-editor ::v-deep .el-input__inner {
					border: 0px solid #ddd;
					border-radius: 0px;
					padding: 0 10px 0 30px;
					box-shadow: none;
					outline: none;
					color: #666;
					width: 100%;
					font-size: 16px;
					border-width: 0 0 1px;
					height: 40px;
				}
				.el-date-editor ::v-deep .el-input__inner[readonly="readonly"] {
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 0 10px 0 30px;
					box-shadow: none;
					outline: none;
					color: #666;
					background: #eee;
					width: 100%;
					font-size: 16px;
					height: 40px;
				}
				::v-deep .el-upload--picture-card {
					background: transparent;
					border: 0;
					border-radius: 0;
					width: auto;
					height: auto;
					line-height: initial;
					vertical-align: middle;
				}
				::v-deep .upload .upload-img {
					border: 1px solid #ddd;
					cursor: pointer;
					border-radius: 0px;
					color: #999;
					width: 80px;
					font-size: 26px;
					line-height: 80px;
					text-align: center;
					height: 80px;
				}
				::v-deep .el-upload-list .el-upload-list__item {
					border: 1px solid #ddd;
					cursor: pointer;
					border-radius: 0px;
					color: #999;
					width: 80px;
					font-size: 26px;
					line-height: 80px;
					text-align: center;
					height: 80px;
					font-size: 14px;
					line-height: 1.8;
				}
				::v-deep .el-upload .el-icon-plus {
					border: 1px solid #ddd;
					cursor: pointer;
					border-radius: 0px;
					color: #999;
					width: 80px;
					font-size: 26px;
					line-height: 80px;
					text-align: center;
					height: 80px;
				}
				::v-deep .el-upload__tip {
					color: #666;
					font-size: 16px;
				}
				.el-textarea ::v-deep .el-textarea__inner {
					border: 1px solid #ddd;
					border-radius: 0px;
					padding: 12px;
					box-shadow: none;
					outline: none;
					color: #666;
					width: 100%;
					font-size: 16px;
					height: auto;
				}
				.el-textarea ::v-deep .el-textarea__inner[readonly="readonly"] {
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 12px;
					box-shadow: none;
					outline: none;
					color: #666;
					width: 100%;
					font-size: 16px;
					height: auto;
				}
				::v-deep .el-input__inner::placeholder {
					color: #123;
					font-size: 16px;
				}
				::v-deep textarea::placeholder {
					color: #123;
					font-size: 16px;
				}
				.editor {
					background-color: #fff;
					border-radius: 0;
					padding: 0;
					box-shadow: none;
					margin: 0;
					width: 100%;
					border-color: #ccc;
					border-width: 0;
					border-style: solid;
					height: auto;
				}
				.editor ::v-deep .ql-toolbar {
					border: 0px solid #ddd;
					background: none;
					border-width: 1px 1px 0;
				}
				.editor ::v-deep .ql-container {
					border: 1px solid #ddd;
					background: none;
					min-height: 180px;
				}
				.editor ::v-deep .ql-container .ql-blank::before {
					color: #999;
				}
				.upload-img {
					object-fit: cover;
					width: 120px;
					height: 120px;
				}
				.viewBtn {
					border: 0;
					cursor: pointer;
					padding: 0 20px;
					margin: 0;
					color: #fff;
					display: inline-block;
					font-size: 14px;
					line-height: 34px;
					border-radius: 2px;
					outline: none;
					background: #05441a;
					width: auto;
					height: 34px;
				}
				.viewBtn:hover {
					opacity: 0.7;
				}
				.unviewBtn {
					border: 0;
					cursor: pointer;
					padding: 0 20px;
					margin: 0;
					color: #fff;
					display: inline-block;
					font-size: 14px;
					line-height: 34px;
					border-radius: 4px;
					outline: none;
					background: #999;
					width: auto;
					height: 34px;
				}
				.unviewBtn:hover {
					opacity: 0.8;
				}
			}
			.add-btn-item {
				padding: 30px 0 0;
				margin: 20px auto;
				display: flex;
				width: 100%;
				clear: both;
				align-items: center;
				text-align: center;
				.submitBtn {
					border: 1px solid #05441a;
					cursor: pointer;
					padding: 0 15px;
					margin: 0 20px 0 0;
					display: inline-block;
					font-size: 14px;
					line-height: 40px;
					border-radius: 0px;
					outline: none;
					background: #05441a;
					width: auto;
					min-width: 110px;
					height: 40px;
					.icon {
						color: rgba(255, 255, 255, 1);
					}
					.text {
						color: rgba(255, 255, 255, 1);
						font-size: 16px;
					}
				}
				.submitBtn:hover {
					opacity: 0.7;
					.icon {
						color: #fff;
					}
					.text {
						color: #fff;
					}
				}
				.closeBtn {
					border: 1px solid #05441a30;
					cursor: pointer;
					padding: 0 20px 0 15px;
					margin: 0 20px 0 0;
					display: inline-block;
					font-size: 16px;
					line-height: 40px;
					border-radius: 0px;
					outline: none;
					background: #05441a10;
					width: auto;
					min-width: 100px;
					height: 40px;
					.icon {
						color: #05441a;
						font-size: 18px;
					}
					.text {
						color: #05441a;
						font-size: 16px;
					}
				}
				.closeBtn:hover {
					opacity: 0.7;
					.icon {
					}
					.text {
					}
				}
			}
		}
	}
	.el-date-editor.el-input {
		width: auto;
	}
</style>
