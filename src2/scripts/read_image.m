pic=imread('sample2.jpg');
pic=rgb2gray(pic);
disp(size(pic));
k=1;
for width=1:480
       for length=1:640
        a(k)=pic(width,length); 
        k=k+1;
       end
end
fid=fopen('image.txt','w');
fprintf(fid,'%x ',a);
disp('Text file write done');
disp(' ');
fclose(fid);
