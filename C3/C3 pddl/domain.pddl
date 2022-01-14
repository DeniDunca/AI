(define (domain messy_house)
	(:requirements :strips)
	(:predicates 
		(at ?c ?x) (next ?from ?to) (holding ?x) (empty-hands ?c) (half-open ?k) (door-between ?x ?y) (dust-in ?x) 
		(cleaner ?c) (trash ?t) (key ?k) (vacuum ?v) (place ?p) (safe-place ?s) (recycle ?t) (open ?x) (empty-sack ?c) (in-sack ?t))

	(:action move
		:parameters (?c ?from ?to)
		:precondition (and (cleaner ?c) (at ?c ?from) (next ?from ?to) (next ?to ?from) (place ?from) (or (place ?to) (safe-place ?to))
						(not (door-between ?from ?to)) (not (door-between ?to ?from)) (not (dust-in ?to)))
		:effect ( and (at ?c ?to) (not (at ?c ?from)))
			 
	)
	
	(:action recycle_trash
	    :parameters (?c ?p ?t)
	    :precondition (and (cleaner ?c) (trash ?t) (safe-place ?p) (in-sack ?t) (at ?c ?p))
	    :effect (and (recycle ?t) (empty-sack ?c) (not (in-sack ?t)))
	    )

	(:action grab_tool
		:parameters (?c ?p ?l)
		:precondition (and (cleaner ?c) (place ?p) (at ?c ?p) (at ?l ?p) (empty-hands ?c) (or (key ?l) (vacuum ?l))
				)
		:effect (and (holding ?l) (not (empty-hands ?c)) (not (at ?l ?p)))
	)

	(:action drop_tool
		:parameters (?c ?p ?l)
		:precondition (and (cleaner ?c) (place ?p) (at ?c ?p) (holding ?l) (or (key ?l) (vacuum ?l)) )
		:effect (and (at ?l ?p) (empty-hands ?c) (not (holding ?l)))
	)

	(:action put_in_sack
		:parameters (?c ?p ?t)
		:precondition (and (cleaner ?c) (trash ?t) (place ?p) (at ?c ?p) (at ?t ?p) (empty-sack ?c))
		:effect ( and (in-sack ?t) (not (empty-sack ?c)) (not (at ?t ?p)))
	)


	(:action open_room
		:parameters (?c ?from ?to ?k)
		:precondition (and (cleaner ?c) (place ?from) (place ?to) (key ?k) (at ?c ?from)  (door-between ?from ?to)
						(holding ?k) (not (open ?k)))
		:effect (and (not (door-between ?from ?to)) (not (door-between ?to ?from))
			(when (half-open ?k) (open ?k)) (when (not (half-open ?k)) (and (half-open ?k))))
	)

	(:action vacuum_dust
		:parameters (?c ?from ?to ?v)
		:precondition (and (cleaner ?c) (place ?from) (place ?to) (next ?from ?to) (next ?to ?from) (vacuum ?v) (at ?c ?from) (dust-in ?to) (holding ?v))
		:effect (and (not (dust-in ?to)))
	)

)


