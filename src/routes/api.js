import { Router } from "express";
const router = Router();

router.get("/business", (req, res) => {
  res.json({ message: "servidors funcionando" });
});

export default router;
