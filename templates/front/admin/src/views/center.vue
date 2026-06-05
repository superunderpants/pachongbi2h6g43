<template>
	<div :style='{"padding":"22px 28px"}'>
		<el-form
			:style='{"border":"0px solid #ddd","padding":"50px 30px","boxShadow":"none","borderRadius":"8px","flexWrap":"wrap","background":"#ffffff","display":"flex"}'
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			label-width="180px"
		>
				<el-form-item :style='{"width":"50%","margin":"10px 0px 10px 0 ","display":"flex"}'   v-if="flag=='yonghu'"  label="账号" prop="zhanghao">
					<el-input v-model="ruleForm.zhanghao" :readonly="ro.zhanghao" placeholder="账号" clearable></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"50%","margin":"10px 0px 10px 0 ","display":"flex"}'   v-if="flag=='yonghu'"  label="姓名" prop="xingming">
					<el-input v-model="ruleForm.xingming" :readonly="ro.xingming" placeholder="姓名" clearable></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"50%","margin":"10px 0px 10px 0 ","display":"flex"}' v-if="flag=='yonghu'"  label="性别" prop="xingbie">
					<el-select filterable v-model="ruleForm.xingbie" :disabled="ro.xingbie" placeholder="请选择性别">
						<el-option
							v-for="(item,index) in yonghuxingbieOptions"
							:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item :style='{"width":"50%","margin":"10px 0px 10px 0 ","display":"flex"}'   v-if="flag=='yonghu'"  label="手机" prop="shouji">
					<el-input v-model="ruleForm.shouji" :readonly="ro.shouji" placeholder="手机" clearable></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"50%","margin":"10px 0px 10px 0 ","display":"flex"}' v-if="flag=='yonghu'" label="头像" prop="touxiang">
					<file-upload
						tip="点击上传头像"
						action="file/upload"
						:limit="1"
						accept="image/*"
						:multiple="false"
						:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
						@change="yonghutouxiangUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item :style='{"width":"50%","margin":"10px 0px 10px 0 ","display":"flex"}' v-if="flag=='users'" label="用户名" prop="username">
					<el-input v-model="ruleForm.username" placeholder="用户名"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"50%","margin":"10px 0px 10px 0 ","display":"flex"}' v-if="flag=='users'" label="头像" prop="image">
					<file-upload
						tip="点击上传头像"
						action="file/upload"
						:limit="1"
						:multiple="false"
						:fileUrls="ruleForm.image?ruleForm.image:''"
						@change="usersimageUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item :style='{"padding":"0 30px","margin":"30px  auto 0 auto","flexWrap":"wrap","background":"none","display":"flex","width":"auto","justifyContent":"center"}'>
					<el-button class="btn3" type="primary" @click="onUpdateHandler">
						<span class="icon iconfont icon-queren15"></span>
						确定 
					</el-button>
				</el-form-item>
		</el-form>
	</div>
</template>
<script>
// 校验引入
	import { 
		isIntNumer,
		isMobile,
	} from "@/utils/validate";

	export default {
		data() {
			return {
				ruleForm: {},
				ro: {},
				flag: '',
				usersFlag: false,
				yonghuxingbieOptions: [],
			};
		},
		mounted() {
			var table = this.$storage.get("sessionTable");
			this.flag = table;
			this.$http({
				url: `${this.$storage.get("sessionTable")}/session`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code === 0) {
					if(table == 'yonghu') {
						this.ro = {
							zhanghao: false,
							mima: false,
							xingming: false,
							xingbie: false,
							shouji: false,
							touxiang: false,
							status: false,
						}
					}

					this.ruleForm = data.data;
				} else {
					this.$message.error(data.msg);
				}
			});
			this.yonghuxingbieOptions = "男,女".split(',')
		},
		methods: {
			yonghutouxiangUploadChange(fileUrls) {
				this.ruleForm.touxiang = fileUrls;
			},
			usersimageUploadChange(fileUrls) {
				this.ruleForm.image = fileUrls;
			},
			onUpdateHandler() {
				if((!this.ruleForm.zhanghao)&& 'yonghu'==this.flag){
					this.$message.error('账号不能为空');
					return
				}
				if((!this.ruleForm.mima)&& 'yonghu'==this.flag){
					this.$message.error('密码不能为空');
					return
				}
				if((!this.ruleForm.xingming)&& 'yonghu'==this.flag){
					this.$message.error('姓名不能为空');
					return
				}
				if((!this.ruleForm.shouji)&& 'yonghu'==this.flag){
					this.$message.error('手机不能为空');
					return
				}
				if('yonghu' ==this.flag && this.ruleForm.shouji&&(!isMobile(this.ruleForm.shouji))){
					this.$message.error(`手机应输入手机格式`);
					return
				}
				if(this.ruleForm.touxiang!=null) {
					this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
				}
				if('yonghu' ==this.flag && this.ruleForm.status&&(!isIntNumer(this.ruleForm.status))){
					this.$message.error(`状态应输入整数`);
					return
				}
				if('users'==this.flag && this.ruleForm.username.trim().length<1) {
					this.$message.error(`用户名不能为空`);
					return	
				}
				if(this.flag=='users'){
					this.ruleForm.image = this.ruleForm.image.replace(new RegExp(this.$base.url,"g"),"")
				}
				this.$http({
					url: `${this.$storage.get("sessionTable")}/update`,
					method: "post",
					data: this.ruleForm
				}).then(({ data }) => {
					if (data && data.code === 0) {
						if(this.flag=='users'){
							this.$storage.set('headportrait',this.ruleForm.image)
						}else {
							if(this.flag == 'yonghu') {
								this.$storage.set('headportrait',this.ruleForm.touxiang)
							}
						}
						this.$message({
							message: "修改信息成功",
							type: "success",
							duration: 1500,
							onClose: () => {
								window.location.reload();
							}
						});
					} else {
						this.$message.error(data.msg);
					}
				});
			},
		}
	};
</script>
<style lang="scss" scoped>
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item ::v-deep .el-form-item__label {
				padding: 0 10px;
				color: #000000;
				white-space: nowrap;
				font-weight: 600;
				width: 180px;
				font-size: 16px;
				line-height: 40px;
				text-align: right;
			}
	
	.add-update-preview .el-form-item ::v-deep .el-form-item__content {
		margin-left: auto !important;
		margin: auto !important;
		flex: 1;
		display: flex;
		width: 100%;
		justify-content: flex-start;
		align-items: flex-start;
		flex-wrap: wrap;
	}
	
	.add-update-preview .el-input ::v-deep .el-input__inner {
				border-radius: 4px;
				padding: 0 12px;
				box-shadow: inset 0px 3px 6px 1px rgba(0,0,0,0.16);
				outline: none;
				color: #333;
				width: 100%;
				font-size: 16px;
				border-width: 0;
				height: 50px;
			}
	
	.add-update-preview .el-select ::v-deep .el-input__inner {
				border-radius: 4px;
				padding: 0 12px;
				box-shadow: inset 0px 3px 6px 1px rgba(0,0,0,0.16);
				outline: none;
				color: #333;
				width: 100%;
				font-size: 16px;
				border-width: 0;
				height: 50px;
			}
	
	.add-update-preview .el-date-editor ::v-deep .el-input__inner {
				border-radius: 4px;
				padding: 0 30px;
				box-shadow: inset 0px 3px 6px 1px rgba(0,0,0,0.16);
				outline: none;
				color: #333;
				width: 100%;
				font-size: 16px;
				border-width: 0;
				height: 50px;
			}
	
	.add-update-preview ::v-deep .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview ::v-deep .el-upload-list .el-upload-list__item {
				border: 1px solid #DADFE6;
				cursor: pointer;
				border-radius: 4px;
				box-shadow: inset 0px 3px 6px 1px rgba(0,0,0,0.16);
				color: #000000;
				font-weight: 600;
				width: 100px;
				font-size: 30px;
				line-height: 100px;
				text-align: center;
				height: 100px;
			}
	
	.add-update-preview ::v-deep .el-upload .el-icon-plus {
				border: 1px solid #DADFE6;
				cursor: pointer;
				border-radius: 4px;
				box-shadow: inset 0px 3px 6px 1px rgba(0,0,0,0.16);
				color: #000000;
				font-weight: 600;
				width: 100px;
				font-size: 30px;
				line-height: 100px;
				text-align: center;
				height: 100px;
			}
	
	.add-update-preview .el-textarea ::v-deep .el-textarea__inner {
				border-radius: 4px;
				padding: 12px;
				box-shadow:  inset 0px 3px 6px 1px rgba(0,0,0,0.16);
				outline: none;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 16px;
				border-color: #555555;
				border-width: 0;
				border-style: solid;
				height: auto;
			}
	
	.add-update-preview .btn3 {
				border: 0px solid #206cb4;
				cursor: pointer;
				padding: 0 24px;
				margin: 4px;
				color: #fff;
				font-weight: bold;
				font-size: 16px;
				border-radius: 24px  24px  24px  24px;
				outline: none;
				background: #10C17C;
				width: auto;
				min-width: 176px;
				height: 47px;
				.iconfont {
						margin: 0 2px;
						color: #fff;
						display: none;
						font-size: 16px;
						height: 40px;
					}
	}
	
	.add-update-preview .btn3:hover {
				opacity: 0.8;
			}
	.editor>.avatar-uploader {
		line-height: 0;
		height: 0;
	}
</style>
