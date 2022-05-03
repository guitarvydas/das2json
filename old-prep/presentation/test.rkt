(define (test x)
    loop
      (incf x) = x + 1
      (format *standard-output* "top of loop ~a~%' x)
      exit when (= x 10)
      (format *standard-output* "loop again~%")
    end loop
(format *standard-output* "done~%"))

