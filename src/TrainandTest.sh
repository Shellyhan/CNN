
#Traning / Predicting the CNN:

#---Set the paths for caffe and logging:
caffe_dir='/usr/local/caffe'
log_dir="log"

if [ ! -d "$log_dir" ]; then
	mkdir $log_dir
fi

#---Traing:
$caffe_dir/bin/caffe.bin train -solver alpha_solver.prototxt -gpu 0

#---Generate log file:
DATA_STR=$(date "+%m_%d_%Y_%H_%M_%S")
LOG_FILE="log_$DATA_STR.txt"

#---Deploy and predict (only uncommend if you have trained the CNN and ready to predict):
#$caffe_dir/bin/caffe.bin test -model alpha_deploy.prototxt -weights alpha_iter_1300.caffemodel -gpu 0 -iterations 48 > "$log_dir/$LOG_FILE"