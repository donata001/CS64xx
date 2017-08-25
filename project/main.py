
import cv2


def get_object_center(img):
    ptx = []
    pty = []
    for i in xrange(img.shape[0]):
        for j in xrange(img.shape[1]):
            if img[i][j].all() != 0:
                ptx.append(i)
                pty.append(j)
    center = (sum(ptx)/len(ptx), sum(pty)/len(pty))
    return center


def crop_object(img, center):
    x_offset = 190
    y_offset = 110
    return img[center[0]-x_offset:center[0]+x_offset, 
               center[1]-y_offset:center[1]+y_offset]



def alpha_blending(top, bottom, insert_y):   
    fixed_x = 1000
    for c in range(0,3):
        alpha = top[:, :, 3] / 255.0
        insert_x = fixed_x + top.shape[0]/2
        bottom[insert_x:insert_x + top.shape[0], insert_y:insert_y+top.shape[1], c] = \
        top[:, :, c] * alpha + \
        bottom[insert_x:insert_x + top.shape[0], insert_y:insert_y+top.shape[1], c] * (1-alpha)
    return bottom
 
 
    
def main():
    for i in xrange(1, 359):
        name1 = str(i) + '.png'
        name2 = '{0:04d}.png'.format(i)
        black = cv2.imread("blender_source/" + name1, -1)  
        bottom = cv2.imread("source/frame" + name2, -1)
        center = get_object_center(black)
        top_layer = crop_object(black, center)
        #cv2.imwrite('tmp0.png', top_layer)
        relative_y = (center[1]-top_layer.shape[1]/2) *1.0 / black.shape[1]
        insert_y = int(relative_y * bottom.shape[1])
        result = alpha_blending(top_layer, bottom, insert_y)
        cv2.imwrite('output/frame{0:04d}.png'.format(i), result)
    
    
    
if __name__ == "__main__":
    main()    
    
    
    
    
    
    