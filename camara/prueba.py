import cv2
import color_tracker

cordenadas = []

def tracker_callback(t: color_tracker.ColorTracker):
    # cv2.imshow("debug frame", tracker.debug_frame)

    # Stop the script when we press ESC
    # key = cv2.waitKey(1)
    # if key == 27:
    #     tracker.stop_tracking()

    # if (tracker.tracked_objects.__sizeof__ > 0)
    #     print(tracker.tracked_objects[0])    

    for obj in tracker.tracked_objects:
        global cordenadas        
        cordenadas = obj.last_point
        # print("El objeto rojo esta en: {0}".format(cordenadas))  
        tracker.stop_tracking()        

tracker = color_tracker.ColorTracker(max_nb_of_objects=1, max_nb_of_points=1)
tracker.set_tracking_callback(tracker_callback)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30, 27))

with color_tracker.WebCamera() as cam:
    # Define your custom Lower and Upper HSV values
    tracker.track(cam, [0, 21, 154], [2, 192, 255], max_skipped_frames=24,min_contour_area=4000,kernel = kernel)

print("El objeto rojo esta en: {0}".format(cordenadas))